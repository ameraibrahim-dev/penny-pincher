from django.urls import path, include, reverse_lazy
from django.views.generic import TemplateView

from user.views import PasswordResetConfirmView, PasswordChangeView, PasswordResetView, RegistrationView,UserUpdateView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeDoneView, PasswordResetDoneView, \
    PasswordResetCompleteView
from django_registration.backends.activation.views import ActivationView

app_name = "user"

urlpatterns = [
    # login,logout
    path('login/', LoginView.as_view(template_name='user_auth/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='user_auth/logout.html'), name='logout'),
    # password change
    path('password_change/', PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/',
         PasswordChangeDoneView.as_view(template_name='user_auth/password_change_done.html'),
         name='password_change_done'),
    # password reset
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/',
         PasswordResetDoneView.as_view(template_name='user_auth/password_reset_done.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/',
         PasswordResetCompleteView.as_view(template_name='user_auth/password_reset_complete.html'),
         name='password_reset_complete'),

    # register
    path('register/', RegistrationView.as_view(), name='django_registration_register'),
    path('register/complete/', TemplateView.as_view(
        template_name="django_registration/registration_complete.html"
    ), name='django_registration_complete'),
    path('register/closed/', TemplateView.as_view(
        template_name="django_registration/registration_closed.html"
    ), name='django_registration_disallowed'),

    path('activate/complete/', TemplateView.as_view(template_name="django_registration/activation_complete.html"),
         name='django_registration_activation_complete'),
    path('activate/<str:activation_key>/',
         ActivationView.as_view(success_url=reverse_lazy("user:django_registration_activation_complete")),
         name='django_registration_activate'),

    path('profile/', UserUpdateView.as_view(), name='profile'),

]
