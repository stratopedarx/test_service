from django.conf.urls import url

from . import views


app_name = 'quiz'   # namespace for this app
urlpatterns = [
    url(r'^$', views.UserProfileView.as_view(), name='user_profile'),
    url(r'^(?P<type_test_id>\d+)/$', views.quiz_test_view, name='quiz_test'),
]
