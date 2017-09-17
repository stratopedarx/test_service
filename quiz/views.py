from django.views import generic
from django.contrib.auth import logout
from django.http import HttpResponseRedirect


class UserProfileView(generic.ListView):
    pass


class LoginView(generic.TemplateView):
    pass


class LogoutView(generic.View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")


class RegisterView(generic.FormView):
    pass
