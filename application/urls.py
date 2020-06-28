from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('home.urls'), name='home'),  # the app for home page and system authorization
    url(r'^quiz/', include('quiz.urls'), name='quiz'),  # the custom side
    url(r'^admin/', admin.site.urls),
]
