from django.contrib.auth import authenticate
from django_registration.backends.activation.views import RegistrationView
from .forms import UserRegistrationForm
from django_registration import signals
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView, PasswordResetView,PasswordResetConfirmView


# Create your views here.
class RegistrationView(RegistrationView):
    email_body_template='django_registration/activation_email_body.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy("accounts:django_registration_complete")



class PasswordChangeView(PasswordChangeView):
    template_name = 'accounts_auth/password_change_form.html'
    success_url = reverse_lazy('accounts:password_change_done')


class PasswordResetView(PasswordResetView):
    email_template_name = 'accounts_auth/password_reset_email.html'
    subject_template_name = 'accounts_auth/password_reset_subject.txt'
    success_url = reverse_lazy('accounts:password_reset_done')
    template_name = 'accounts_auth/password_reset_form.html'

class PasswordResetConfirmView(PasswordResetConfirmView):
    success_url = reverse_lazy('accounts:password_reset_complete')
    template_name = 'accounts_auth/password_reset_confirm.html'
