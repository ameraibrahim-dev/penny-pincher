from django.contrib.auth.views import LogoutView, PasswordChangeDoneView
from django.urls import path, reverse_lazy
from django.views.generic import TemplateView
from django_registration.backends.activation.views import ActivationView

from user.views import PasswordResetConfirmView, PasswordChangeView, PasswordResetView, RegistrationView, \
    UserUpdateView, LoginView, PasswordResetCompleteView

app_name = "user"

urlpatterns = [
    # login,logout
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # password change
    path('password_change/', PasswordChangeView.as_view(), name='password_change'),
    # password reset
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),

    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # register
    path('register/', RegistrationView.as_view(), name='django_registration_register'),
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
