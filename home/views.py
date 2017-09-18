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

from .models import User
from home.forms.user import LoginForm, RegisterForm, RestorePasswordRequestForm


def redirect_if_user_login(f):
    # Redirects from home and register pages if the user is already authorized
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated():
            # return an absolute link
            return HttpResponseRedirect(reverse('quiz:user_profile'))
        else:
            return f(request, *args, **kwargs)
    return wrap


class IndexView(generic.TemplateView):
    template_name = 'home/index.html'


class LoginView(generic.TemplateView):
    form_class = LoginForm
    template_name = 'home/login.html'

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
                _next = request.GET.get('next', reverse('quiz:user_profile'))
                return HttpResponseRedirect(_next, status=301)
            else:
                errors = [_('LOGIN FAILD')]
        return self.render_to_response(locals())


class LogoutView(generic.View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')


class RegisterView(generic.FormView):
    form_class = RegisterForm
    template_name = 'home/register.html'
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
    template_name = 'home/success_register.html'


class UserSettingsView(LoginRequiredMixin, generic.DetailView):
    template_name = 'home/settings.html'
    model = get_user_model()
    context_object_name = 'user'

    def get_object(self, queryset=None):
        return User.objects.get(id=self.request.user.id)


class RestorePasswordRequestView(generic.FormView):
    form_class = RestorePasswordRequestForm
    template_name = 'home/change_password.html'

    def form_valid(self, form):
        email = form.cleaned_data['email']
        new_password = ''.join(map(lambda x: random.choice(string.ascii_letters + string.digits), range(10)))

        user = get_user_model().objects.get(email=email)
        user.set_password(new_password)
        user.save()
        messages.add_message(self.request, messages.SUCCESS,
                             _('Your password is reset. Check email and login.'))
        return HttpResponseRedirect(reverse('home:login'))
