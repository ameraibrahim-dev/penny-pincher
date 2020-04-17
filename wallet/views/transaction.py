from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from wallet.forms import WalletTransactionForm
from wallet.models import Wallet, WalletTransaction


class CreateTransactionView(LoginRequiredMixin, CreateView):
    model = WalletTransaction
    form_class = WalletTransactionForm
    template_name = 'wallet_transaction/create_transaction.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        wallet_pk = self.kwargs.get('pk')
        wallet = Wallet.objects.get(owner=self.request.user, pk=wallet_pk)
        instance.wallet = wallet
        return super(CreateTransactionView, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(CreateTransactionView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        kwargs.update(self.kwargs)
        return kwargs


class OverviewPageCreateTransaction(CreateTransactionView):

    def get_success_url(self):
        return reverse_lazy('wallet:wallet_overview', kwargs={'pk': self.get_object().wallet.pk})


class TransactionPageCreateTransaction(CreateTransactionView):
    def get_success_url(self):
        return reverse_lazy('wallet:wallet_overview', kwargs={'pk': self.get_object().wallet.pk})
