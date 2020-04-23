from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

from wallet.forms import WalletCreateForm, WalletUpdateForm
from wallet.models import Wallet


class WalletListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        return Wallet.objects.filter(owner=self.request.user)


class WalletDetailView(LoginRequiredMixin, DetailView):
    model = Wallet

    def get_queryset(self):
        return Wallet.objects.filter(owner=self.request.user)

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(WalletOverview, self).form_valid(form)


class WalletOverview(WalletDetailView):
    template_name = 'wallet/overview.html'


class WalletSettingsView(WalletDetailView):
    template_name = 'wallet/settings.html'


class WalletTransactionsView(WalletDetailView):
    template_name = 'wallet/transactions.html'


class CreateWalletView(LoginRequiredMixin, CreateView):
    model = Wallet
    form_class = WalletCreateForm
    template_name = 'wallet/create_wallet_form.html'
    success_url = reverse_lazy('wallet:wallet_list')

    def get_queryset(self):
        return Wallet.objects.filter(owner=self.request.user)

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        name = form.cleaned_data.get('name')
        wallet_type = form.cleaned_data.get('type')
        if Wallet.objects.filter(owner=self.request.user, type=wallet_type, name=name):
            form.add_error('name', 'This wallet is duplicated')
            return self.form_invalid(form)
        return super(CreateWalletView, self).form_valid(form)


class UpdateWalletView(LoginRequiredMixin, UpdateView):
    form_class = WalletUpdateForm
    template_name = 'wallet/update_wallet_form.html'

    def get_queryset(self):
        return Wallet.objects.filter(owner=self.request.user)

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        name = form.cleaned_data.get('name')
        wallet_type = form.cleaned_data.get('type')
        if Wallet.objects.filter(owner=self.request.user, type=wallet_type, name=name):
            form.add_error('name', 'This wallet is duplicated')
            return self.form_invalid(form)
        return super(UpdateWalletView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('wallet:update_wallet', kwargs={'pk': self.get_object().pk}, )


class DeleteWalletView(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy('wallet:wallet_list')

    def get_queryset(self):
        return Wallet.objects.filter(owner=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
