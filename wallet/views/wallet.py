from msilib.schema import ListView

from django.contrib.auth.mixins import LoginRequiredMixin

from wallet.models import Wallet


class WalletListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        return Wallet.objects.filter(owner=self.request.user)