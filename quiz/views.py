import random
import string

from django.views import generic
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout, authenticate, login, get_user_model

from .models import User, Question, Option, TypeTest
from quiz.forms.quiz.user import (LoginForm, RegisterForm, AddUserItemIntoGroupForm,
                                  RestorePasswordRequestForm)


def redirect_if_user_login(f):
    # Redirects from home and register pages if the user is already authorized
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated():
            # return an absolute link
            return HttpResponseRedirect(reverse('quiz:userprofile'))
        else:
            return f(request, *args, **kwargs)
    return wrap


class LoginView(generic.TemplateView):
    form_class = LoginForm
    template_name = 'quiz/login.html'

    @method_decorator(redirect_if_user_login)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(request.POST or None)
        return self.render_to_response(locals())

    def post(self, request):
        form = self.form_class(request.POST or None)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(**data)
            if user and user.is_active:
                login(request, user)
                next = self.request.GET.get('next', reverse('quiz:userprofile'))
                return HttpResponseRedirect(next, status=301)
            else:
                errors = [_('LOGIN FAILD')]
        return self.render_to_response(locals())


class LogoutView(generic.View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')


class RegisterView(generic.FormView):
    form_class = RegisterForm
    template_name = 'quiz/register.html'
    success_url = '/quiz/'

    @method_decorator(redirect_if_user_login)
    def dispatch(self, request, *args, **kwargs):
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        instance = form.save()
        instance.is_active = True
        instance.set_password(form.cleaned_data['password'])
        instance.save()
        user = authenticate(username=instance.username, password=form.cleaned_data['password'])
        login(self.request, user)
        messages.add_message(self.request, messages.SUCCESS, _('You have successfully registered'))
        return super(RegisterView, self).form_valid(form)


class RegisterSuccessView(generic.TemplateView):
    template_name = 'quiz/success_register.html'


class UserProfileView(LoginRequiredMixin, generic.ListView):
    """Show list of available tests on the user page """
    template_name = 'quiz/home.html'
    model = TypeTest

    def get_queryset(self):
        qs = super(UserProfileView, self).get_queryset()
        return qs

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        available_tests = super(UserProfileView, self).get_queryset()
        context['tests'] = available_tests
        return context


class UserSettingsView(LoginRequiredMixin, generic.DetailView):
    template_name = 'quiz/settings.html'
    model = get_user_model()
    context_object_name = 'user'

    def get_object(self, queryset=None):
        return User.objects.get(id=self.request.user.id)


class RestorePasswordRequestView(generic.FormView):
    form_class = RestorePasswordRequestForm
    template_name = 'quiz/change_password.html'

    def form_valid(self, form):
        email = form.cleaned_data['email']
        new_password = ''.join(map(lambda x: random.choice(string.ascii_letters + string.digits), range(10)))

        user = get_user_model().objects.get(email=email)
        user.set_password(new_password)
        user.save()
        messages.add_message(self.request, messages.SUCCESS,
                             _('Your password is reset. Check email and login.'))
        return HttpResponseRedirect(reverse('quiz:login'))
