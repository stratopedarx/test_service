from django.contrib import admin

from .models import Question, Option, TypeTest


admin.site.register(Question)
admin.site.register(Option)
admin.site.register(TypeTest)
