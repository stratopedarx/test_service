import random

from django.contrib import auth
from django.views import generic
from django.http.response import Http404
from django.contrib.auth import get_user_model
from django.template.context_processors import csrf
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404

from home.models import User
from .models import Question, Option, TypeTest, CurrentUserResult


class UserProfileView(LoginRequiredMixin, generic.ListView):
    """Show list of available tests on the user page """
    template_name = 'quiz/home.html'
    model = TypeTest

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        available_tests = super(UserProfileView, self).get_queryset()
        context['type_tests'] = available_tests
        return context


class UserSettingsView(LoginRequiredMixin, generic.DetailView):
    template_name = 'quiz/settings.html'
    model = get_user_model()
    context_object_name = 'user'

    def get_object(self, queryset=None):
        return User.objects.get(id=self.request.user.id)


def get_random_question_and_options(type_test_id):
    """Takes random question and related options from DataBase."""
    # TODO: fetches only those questions which are not passed by the user
    questions = list(Question.objects.filter(type_test_id=type_test_id))[:10]
    random.shuffle(questions)
    try:
        question = questions[0]  # temporary solution. Unfortunately we can get the same questions
    except IndexError as ex:
        raise Http404('Question does nor exist!')

    # fetches related options
    options = Option.objects.filter(question_id=question.id)

    return {'question': question, 'options': options}


def quiz_test_view(request, type_test_id):
    """This view shows the page with question and options."""
    context = {}
    context.update(csrf(request))
    user_id = auth.get_user(request).id

    if request.method == 'POST' and request.POST.get('option') is not None:
        # continue the test until we get 5 questions
        current_user_result = get_object_or_404(CurrentUserResult, user_id=user_id)
        current_user_result.results += 1  # increase the number of questions

        # check all choices
        if all(Option.objects.get(id=o).truth for o in request.POST.getlist('option')):
            current_user_result.right_answers += 1
        current_user_result.save()

        if current_user_result.results > 5:
            # prepare result page for the user
            right_answers = current_user_result.right_answers - 1
            results = current_user_result.results - 1
            context = {
                'right_answers': right_answers,
                'results': results,
                'percentage': (right_answers / results) * 100
            }
            current_user_result.delete()  # delete temporary result
            return render('quiz/result.html', context)
    elif request.method == 'POST' and request.POST.get('option') is None:
        current_user_result = CurrentUserResult.objects.get_or_create(user_id=user_id)[0]
        context['error_message'] = 'The option was not chosen. Try again.'
    else:
        # start to test, create temporary current user result
        try:
            current_user_result = CurrentUserResult.objects.get(user_id=user_id)
        except CurrentUserResult.DoesNotExist as ex:
            [c.delete() for c in CurrentUserResult.objects.all()]  # clean database
            current_user_result = CurrentUserResult.objects.create(user_id=user_id)

        if current_user_result.results != 1:
            context['error_message'] = 'The option was not chosen. Try again.'

    context['type_test_id'] = type_test_id
    context['num_question'] = current_user_result.results
    context.update(get_random_question_and_options(type_test_id))

    return render('quiz/test.html', context)
