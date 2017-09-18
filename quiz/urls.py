from django.conf.urls import url

from . import views


app_name = 'quiz'   # namespace for this app
urlpatterns = [
    url(r'^$', views.UserProfileView.as_view(), name='userprofile'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^register/$', views.RegisterView.as_view(), name='register'),
    url(r'^register/success/$', views.RegisterSuccessView.as_view(), name='success_register'),
    url(r'^settings/$', views.UserSettingsView.as_view(), name='settings'),
    url(r'^change/password/$', views.RestorePasswordRequestView.as_view(), name='change_password'),
    # url(r'^(?P<type_test_id>\d+)/(?P<page>\d+)/$', views.QuizTestView.as_view(), name='quiz_test'),
    url(r'^(?P<type_test_id>\d+)/(?P<page>\d+)/$', views.quiz_test_view, name='quiz_test'),
    url(r'^submit/$', views.save_answer, name='submit'),
]
