from django.urls import path, include, reverse_lazy
app_name = "wallet"

urlpatterns = [
    # login,logout
    path('login/', LoginView.as_view(template_name='user_auth/login.html'), name='login'),
]
