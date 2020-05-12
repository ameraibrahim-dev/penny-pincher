from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView, PasswordResetView, PasswordResetConfirmView, LoginView, \
    PasswordResetDoneView, PasswordResetCompleteView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django_registration.backends.activation.views import RegistrationView

from .forms import UserRegistrationForm, LoginForm, PasswordResetForm
# Create your views here.
from .models import User


class LoginView(LoginView):
    template_name = 'user_auth/login.html'
    form_class = LoginForm


class RegistrationView(RegistrationView):
    email_body_template = 'django_registration/activation_email_body.html'
    form_class = UserRegistrationForm
    success_template = 'django_registration/registration_complete.html'

    def form_valid(self, form):
        user = self.register(form)
        user.password = None
        success_context = {'user': user}
        return render(self.request, self.success_template, context=success_context)


class PasswordChangeView(PasswordChangeView):
    template_name = 'user_auth/password_change_form.html'
    success_url = reverse_lazy('user:password_change')

    def form_valid(self, form):
        messages.success(self.request, "Password Change Successful")
        return super(PasswordChangeView, self).form_valid(form)

class PasswordResetView(PasswordResetView):
    email_template_name = 'user_auth/password_reset_email.html'
    subject_template_name = 'user_auth/password_reset_subject.txt'
    form_class = PasswordResetForm
    success_template = 'user_auth/password_reset_done.html'
    template_name = 'user_auth/password_reset_form.html'

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            form.add_error('email', 'User does not exist')
            return self.form_invalid(form)
        opts = {
            'use_https': self.request.is_secure(),
            'token_generator': self.token_generator,
            'from_email': self.from_email,
            'email_template_name': self.email_template_name,
            'subject_template_name': self.subject_template_name,
            'request': self.request,
            'html_email_template_name': self.html_email_template_name,
            'extra_email_context': self.extra_email_context,
        }
        form.save(**opts)
        success_context = {'email': email}
        return render(self.request, self.success_template, context=success_context)


class PasswordResetDoneView(PasswordResetDoneView):
    template_name = 'user_auth/password_reset_done.html'


class PasswordResetConfirmView(PasswordResetConfirmView):
    success_url = reverse_lazy('user:password_reset_complete')
    template_name = 'user_auth/password_reset_confirm.html'


class PasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'user_auth/password_reset_complete.html'


class UserUpdateView(UpdateView, LoginRequiredMixin):
    model = User
    fields = ['first_name', 'last_name']
    template_name = 'user/user_profile.html'
    success_url = reverse_lazy('user:profile')

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, "Update Successful")
        return super(UserUpdateView, self).form_valid(form)
