from django.urls import path, include, reverse_lazy
from .views import *

app_name = "wallet"

urlpatterns = [
    #wallets
    path('overview/<int:pk>/', WalletOverview.as_view(), name='wallet_overview'),
    path('settings/<int:pk>/', WalletSettingsView.as_view(), name='wallet_settings'),
    path('transactions/<int:pk>/', WalletTransactionsView.as_view(), name='wallet_transactions'),
    path('list/', WalletListView.as_view(), name='wallet_list'),
    path('create/', CreateWalletView.as_view(), name='create_wallet'),
    path('update/<int:pk>/', UpdateWalletView.as_view(), name='update_wallet'),
    path('delete/<int:pk>/', DeleteWalletView.as_view(), name='delete_wallet'),
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
