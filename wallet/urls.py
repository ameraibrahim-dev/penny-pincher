from django.urls import path

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
    path('transaction/create/<int:pk>/', CreateTransactionView.as_view(),
         name='wallet_create_transaction'),
    path('transaction/update/<int:pk>/', UpdateTransactionView.as_view(),
         name='wallet_update_transaction'),
    path('transaction/delete/<int:pk>/', DeleteTransactionView.as_view(),
         name='wallet_delete_transaction'),
]
