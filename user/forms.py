from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Invisible
from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.core.validators import EmailValidator
from django.forms import EmailField
from django_registration.forms import RegistrationForm

from .models import User


class LoginForm(AuthenticationForm):
    reCAPTCHA = ReCaptchaField(widget=ReCaptchaV2Invisible)
    username = EmailField(label='Email', validators=[EmailValidator])

    error_messages = {
        'invalid_login': 'Please enter a correct %(username)s and password.',
        'inactive': 'This account is inactive.',
    }

    class Meta:
        fields = ['username', 'password', 'reCAPTCHA']


class PasswordResetForm(PasswordResetForm):
    reCAPTCHA = ReCaptchaField(widget=ReCaptchaV2Invisible)

    class Meta:
        fields = ['email', 'reCAPTCHA']


class UserRegistrationForm(RegistrationForm):
    reCAPTCHA = ReCaptchaField(widget=ReCaptchaV2Invisible)
    first_name = forms.CharField(max_length=30, required=True, min_length=2)
    last_name = forms.CharField(max_length=30, required=True, min_length=2)
    field_order = ['email', 'first_name', 'last_name', 'password1', 'password2', 'reCAPTCHA']
    email=forms.CharField(validators=[EmailValidator])
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2', 'reCAPTCHA']

    def save(self, commit=True):
        instance = super(UserRegistrationForm, self).save(commit=False)
        instance.first_name = self.cleaned_data.get("first_name")
        instance.last_name = self.cleaned_data.get("last_name")
        if commit:
            instance.save()
        return instance
