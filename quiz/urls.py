from django.conf.urls import url

from . import views


app_name = 'quiz'   # namespace for this app
urlpatterns = [
    url(r'^$', views.UserProfileView.as_view(), name='userprofile'),
    # url(r'^(?P<type_test_id>\d+)/(?P<page>\d+)/$', views.QuizTestView.as_view(), name='quiz_test'),
    url(r'^(?P<type_test_id>\d+)/(?P<page>\d+)/$', views.quiz_test_view, name='quiz_test'),
    url(r'^submit/$', views.save_answer, name='submit'),
]
