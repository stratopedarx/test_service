from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import (UserCreationForm as DjangoUserCreationForm,
                                       UserChangeForm as DjangoUserChangeForm)

from quiz.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=32,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Username'),
                'style': 'width: 350px;'
            }),
        required=True,
        label=''
    )
    password = forms.CharField(
        max_length=32,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Password'),
                'style': 'width: 350px;'
            }),
        required=True,
        label=''
    )


class RegisterForm(forms.ModelForm):
    password =forms.CharField(
        max_length=32,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Password'),
                'style': 'width: 350px;'
            }),
        required=True,
        label='')
    required_css_class = 'required'

    class Meta:
        exclude = [
            'date_joined', 'last_login',
            'is_active', 'is_staff', 'is_superuser',
            'first_name', 'last_name',
            'groups', 'user_permissions'
        ]
        model = get_user_model()
        labels = {
            'username': '',
            'email': '',
        }
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Username'),
                    'style': 'width: 350px;'
                }),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Email'),
                    'style': 'width: 350px;'
                }),
        }


class UserChangeForm(DjangoUserChangeForm):
    class Meta:
        model = User
        exclude = ('date_joined',)


class UserCreationForm(DjangoUserCreationForm):
    class Meta:
        model = User
        fields = ('username',)


class AddUserItemIntoGroupForm(forms.Form):
    url = forms.URLField(
        required=True,
        widget=forms.URLInput(attrs={'required': True})
    )
    group_id = forms.IntegerField(required=True, widget=forms.HiddenInput)


class RestorePasswordRequestForm(forms.Form):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Your email'),
                'style': 'width: 350px;'
            }),
        label='',)

