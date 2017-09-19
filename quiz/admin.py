from django import forms
from django.contrib import admin

from .models import Question, Option, TypeTest


# https://stackoverflow.com/questions/6628404/how-to-validate-data-of-two-models-in-the-django-admin-when-using-inlines
class OptionInlineFormset(forms.models.BaseInlineFormSet):
    def clean(self):
        """
        Override clean. Check that at least one correct answer.
        Check that not all the answers are correct.
        """
        # filter out all None
        all_options = list(filter(
            lambda t: t is False or t is True,
            [truth.get('truth') for truth in self.cleaned_data]
        ))
        num_of_truth = all_options.count(True)
        if len(all_options) == num_of_truth or num_of_truth == 0:
            raise forms.ValidationError(
                'At least one answer must be correct. All the answers can\'t be correct.')


class OptionInline(admin.StackedInline):
    model = Option
    extra = 3
    formset = OptionInlineFormset


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
