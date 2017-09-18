from django.conf.urls import url

from . import views


app_name = 'home'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),  # home/main page
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^register/$', views.RegisterView.as_view(), name='register'),
    url(r'^register/success/$', views.RegisterSuccessView.as_view(), name='success_register'),
    url(r'^settings/$', views.UserSettingsView.as_view(), name='settings'),
    url(r'^change/password/$', views.RestorePasswordRequestView.as_view(), name='change_password'),
]
