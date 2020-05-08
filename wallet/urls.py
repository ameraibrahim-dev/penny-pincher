from django.urls import path, include, reverse_lazy
from .views import *

app_name = "wallet"

urlpatterns = [
    # wallets
    path('overview/<int:pk>/', WalletOverview.as_view(), name='wallet_overview'),
    path('wallet_transaction/<int:pk>/', WalletTransactionsView.as_view(), name='wallet_transactions'),
    path('list/', WalletListView.as_view(), name='wallet_list'),
    path('create/', CreateWalletView.as_view(), name='create_wallet'),
    path('update/<int:pk>/', UpdateWalletView.as_view(), name='update_wallet'),
    path('delete/<int:pk>/', DeleteWalletView.as_view(), name='delete_wallet'),
    # wallet wallet_transaction
    path('transaction/create/<int:pk>/', TransactionPageCreateTransaction.as_view(),
         name='wallet_transactions_create_transaction'),
    path('transaction/update/<int:pk>/', TransactionPageUpdateTransaction.as_view(),
         name='wallet_transactions_update_transaction'),
    path('transaction/delete/<int:pk>/', TransactionPageDeleteTransaction.as_view(),
         name='wallet_transactions_delete_transaction'),
    path('overview/create/<int:pk>/', OverviewPageCreateTransaction.as_view(),
         name='wallet_overview_create_transaction'),
    path('overview/update/<int:pk>/', OverviewPageUpdateTransaction.as_view(),
         name='wallet_overview_update_transaction'),
    path('overview/delete/<int:pk>/', OverviewPageDeleteTransaction.as_view(),
         name='wallet_overview_delete_transaction'),
]
