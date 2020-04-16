from captcha.fields import ReCaptchaField
from django_registration.forms import RegistrationForm
from .models import User
from captcha.widgets import ReCaptchaV2Checkbox
from django import forms


class UserRegistrationForm(RegistrationForm):
    reCAPTCHA = ReCaptchaField(widget=ReCaptchaV2Checkbox)
    first_name = forms.CharField(max_length=30, required=True, min_length=2)
    last_name = forms.CharField(max_length=30, required=True, min_length=2)
    field_order = ['email', 'first_name', 'last_name', 'password1', 'password2', 'reCAPTCHA']

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
