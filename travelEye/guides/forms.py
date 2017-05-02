from django.contrib.auth import get_user_model
from django import forms
from django.forms.forms import NON_FIELD_ERRORS
from django.forms import ModelForm

from  . import models

class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username',
        max_length=128
    )

    password= forms.CharField(
        label='Password',
        max_length=128,
        widget=forms.PasswordInput()
    )

class PasswordForm(forms.Form):
    password= forms.CharField(
        label='Enter Password',
        max_length=128,
        widget=forms.PasswordInput()
    )

    password2= forms.CharField(
        label='Re-enter Password',
        max_length=128,
        widget=forms.PasswordInput()
    )

    def clean_password2(self):
        password= self.cleaned_data.get('password', '')
        password2=self.cleaned_data['password2']
        if password != password2:
            raise forms.ValidationError('Password entries do not match.')
        return password2

