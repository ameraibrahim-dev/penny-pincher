from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django_registration.backends.activation.views import RegistrationView
from .forms import UserRegistrationForm, LoginForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView, PasswordResetView, PasswordResetConfirmView, LoginView

# Create your views here.
from .models import User

class LoginView(LoginView):
    template_name = 'user_auth/login.html'
    form_class=LoginForm


class RegistrationView(RegistrationView):
    email_body_template = 'django_registration/activation_email_body.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy("user:django_registration_complete")


class PasswordChangeView(PasswordChangeView):
    template_name = 'user_auth/password_change_form.html'
    success_url = reverse_lazy('user:password_change_done')


class PasswordResetView(PasswordResetView):
    email_template_name = 'user_auth/password_reset_email.html'
    subject_template_name = 'user_auth/password_reset_subject.txt'
    success_url = reverse_lazy('user:password_reset_done')
    template_name = 'user_auth/password_reset_form.html'


class PasswordResetConfirmView(PasswordResetConfirmView):
    success_url = reverse_lazy('user:password_reset_complete')
    template_name = 'user_auth/password_reset_confirm.html'


class UserUpdateView(UpdateView, LoginRequiredMixin):
    model = User
    fields = ['first_name', 'last_name']
    template_name = 'user/user_profile.html'
    success_url = reverse_lazy('user:profile')

    def get_object(self):
        return self.request.user
