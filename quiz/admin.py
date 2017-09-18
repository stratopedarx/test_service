from django.contrib import admin

from .models import Question, Option, TypeTest


class OptionInline(admin.StackedInline):
    model = Option
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionInline]


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 5


class TypeTestAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]


admin.site.register(Option)
admin.site.register(Question, QuestionAdmin)
admin.site.register(TypeTest, TypeTestAdmin)
