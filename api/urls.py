from django.urls import path, include, reverse_lazy
from .views import *

app_name = "api"

urlpatterns = [
    path('v1/user/expenses/categories/', AllExpenseCategoryJsonList.as_view(),
         name='expense_categories_by_user'),
    path('v1/user/earnings/categories/', AllEarningsCategoryJsonList.as_view(),
         name='earnings_categories_by_user'),
    path('v1/user/used/categories/', AllUsedCategoryJsonList.as_view(),
         name='used_categories'),
    path('v1/user/wallet/transactions/list/', WalletTransactionsByUser.as_view(),
         name='wallet_transactions_by_user'),
]
