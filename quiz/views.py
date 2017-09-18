import random

from django.views import generic
from django.contrib.auth import get_user_model
from django.shortcuts import render_to_response
from django.contrib.auth.mixins import LoginRequiredMixin

from home.models import User
from .models import Question, Option, TypeTest, Result


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


class QuizTestView(LoginRequiredMixin, generic.ListView):
    template_name = 'quiz/test.html'
    model = Option

    def get_context_data(self, **kwargs):
        context = super(QuizTestView, self).get_context_data(**kwargs)
        all_options = Option.objects.filter(question__type_test_id=self.kwargs['type_test_id'])
        all_questions = Question.objects.filter(type_test_id=self.kwargs['type_test_id'])
        random.shuffle(list(all_questions))
        question = all_questions[0]
        context['options'] = all_options.filter(question_id=question.id)
        context['question'] = question

        return context


def quiz_test_view(request, type_test_id, page):
    context = {}
    number_questions = 10  # default number of questions
    questions = list(Question.objects.filter(type_test_id=type_test_id)[:number_questions])  # fetch questions
    random.shuffle(questions)  # shuffle list of questions

    options = Option.objects.filter(question_id=question.id)
    page = int(page)
    page += 1
    context['options'] = options
    # context['question'] = question
    context['page'] = page
    return render_to_response('quiz/test.html', context)


def save_answer(request):
    option_id = request.POST['option']
    result = Result.objects.create()
    result.result += 1
    if Option.objects.get(id=option_id).truth:
        result.right_answer += 1
    result.save()
    if result.result == 10:
        return 'result page'
    return ''
