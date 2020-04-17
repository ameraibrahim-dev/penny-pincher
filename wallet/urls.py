from django.urls import path, include, reverse_lazy
from .views import *

app_name = "wallet"

urlpatterns = [
    #wallets
    path('wallet/overview/', WalletOverview.as_view(), name='wallet_overview'),
    path('wallet/settings/', WalletSettingsView.as_view(), name='wallet_settings'),
    path('wallet/transactions/', WalletTransactionsView.as_view(), name='wallet_transactions'),
    path('wallet/create/', CreateWalletView.as_view(), name='create_wallet'),
    path('wallet/update/', UpdateWalletView.as_view(), name='update_wallet'),
    path('wallet/delete/', DeleteWalletView.as_view(), name='delete_wallet'),
    # categories
    path('custom/category/list/', CustomCategoryListView.as_view(), name='custom_categories_list'),
    path('custom/category/create/', CreateCustomCategoryView.as_view(), name='create_custom_categories'),
    path('custom/category/update/<int:pk>/', UpdateCustomCategoryView.as_view(), name='update_custom_categories'),
    path('custom/category/delete/<int:pk>/', DeleteCustomCategoryView.as_view(), name='delete_custom_categories_list'),
    path('predefined/earnings/category/list/', DefinedEarningsCategories.as_view(),
         name='predefined_earnings_categories_list'),
    path('predefined/expenses/category/list/', DefinedExpensesCategories.as_view(),
         name='predefined_expenses_categories_list'),
]
