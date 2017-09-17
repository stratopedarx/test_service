from django.contrib import admin

from .models import User, Question, Option, TypeTest

admin.site.register(User)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(TypeTest)
