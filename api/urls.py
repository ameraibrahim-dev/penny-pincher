from django.urls import path, include, reverse_lazy
from .views import *

app_name = "api"

urlpatterns = [
    path('user/expenses/categories/', AllExpenseCategoryJsonList.as_view(),
         name='all_expenses_categories'),
    path('user/earnings/categories/', AllEarningsCategoryJsonList.as_view(),
         name='all_earnings_categories'),
]
