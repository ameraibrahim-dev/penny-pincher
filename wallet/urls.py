from django.urls import path, include, reverse_lazy
from .views import *

app_name = "wallet"

urlpatterns = [
    # wallets
    path('overview/<int:pk>/', WalletOverview.as_view(), name='wallet_overview'),
    path('settings/<int:pk>/', WalletSettingsView.as_view(), name='wallet_settings'),
    path('wallet_transaction/<int:pk>/', WalletTransactionsView.as_view(), name='wallet_transactions'),
    path('list/', WalletListView.as_view(), name='wallet_list'),
    path('create/', CreateWalletView.as_view(), name='create_wallet'),
    path('update/<int:pk>/', UpdateWalletView.as_view(), name='update_wallet'),
    path('delete/<int:pk>/', DeleteWalletView.as_view(), name='delete_wallet'),
    # wallet wallet_transaction
    path('transactions/create/<int:pk>/', TransactionPageCreateTransaction.as_view(),
         name='wallet_transactions_create_transaction'),
    path('overview/create/<int:pk>/', OverviewPageCreateTransaction.as_view(),
         name='wallet_overview_create_transaction'),
]
