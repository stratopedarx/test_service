import random

from django.contrib import auth
from django.views import generic
from django.http.response import Http404
from django.contrib.auth import get_user_model
from django.shortcuts import render_to_response
from django.template.context_processors import csrf
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin

from home.models import User
from .models import Question, Option, TypeTest, CurrentUserResult, UserResult


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

    if request.POST:
        # continue the test until we get 5 questions
        try:
            current_user_result = CurrentUserResult.objects.get(user_id=user_id)
        except ObjectDoesNotExist as ex:
            raise Http404('User {} does nor exist in CurrentUserResult model!'.format(user_id))

        current_user_result.results += 1  # increase the number of questions
        if Option.objects.get(id=request.POST['option']).truth:  # check the truth of the answer
            current_user_result.right_answers += 1
        current_user_result.save()

        if current_user_result.results >= 5:
            # prepare result page for the user
            right_answers = current_user_result.right_answers
            results = current_user_result.results
            context = {
                'right_answers': right_answers,
                'results': results,
                'percentage': (right_answers / results) * 100
            }
            current_user_result.delete()  # delete temporary result
            return render_to_response('quiz/result.html', context)
    else:
        # start to test
        try:
            # TODO: Fix this point
            current_user_result = CurrentUserResult.objects.create(user_id=user_id)
        except Exception as ex:
            # if this user is already exist delete him and create new one
            CurrentUserResult.objects.get(user_id=user_id).delete()
            current_user_result = CurrentUserResult.objects.create(user_id=user_id)
        current_user_result.save()

    context['type_test_id'] = type_test_id
    context.update(get_random_question_and_options(type_test_id))

    return render_to_response('quiz/test.html', context)

