from django.contrib import admin
from django.urls import path, include
from .views import DashboardView

handler404 = 'penny_pincher.views.custom_page_not_found_view'
handler500 = 'penny_pincher.views.custom_error_view'
handler403 = 'penny_pincher.views.custom_permission_denied_view'
handler400 = 'penny_pincher.views.custom_bad_request_view'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', DashboardView.as_view(), name='dashboard'),
    path('user/', include('user.urls', namespace='user')),
    path('wallet/', include('wallet.urls', namespace='wallet')),
    path('goal/', include('goal.urls', namespace='goal')),
    path('category/', include('category.urls', namespace='category')),
    path('api/', include('api.urls', namespace='api')),
]
