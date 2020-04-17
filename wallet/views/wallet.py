from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

from wallet.forms import WalletCreateForm
from wallet.models import Wallet


class WalletListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        return Wallet.objects.filter(owner=self.request.user)


class WalletOverview(LoginRequiredMixin, DetailView):
    def get_queryset(self):
        return Wallet.objects.filter(owner=self.request.user)

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.store.owner = self.request.user
        return super(WalletOverview, self).form_valid(form)


class WalletSettingsView(LoginRequiredMixin, DetailView):
    def get_queryset(self):
        return Wallet.objects.filter(owner=self.request.user)

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.store.owner = self.request.user
        return super(WalletSettingsView, self).form_valid(form)


class WalletTransactionsView(LoginRequiredMixin, DetailView):
    def get_queryset(self):
        return Wallet.objects.filter(owner=self.request.user)

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.store.owner = self.request.user
        return super(WalletTransactionsView, self).form_valid(form)


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
        return super(CreateWalletView, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(CreateWalletView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        kwargs.update(self.kwargs)
        return kwargs


class UpdateWalletView(LoginRequiredMixin, UpdateView):
    def get_queryset(self):
        return Wallet.objects.filter(owner=self.request.user)

    def get_form_kwargs(self):
        kwargs = super(UpdateWalletView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        kwargs.update(self.kwargs)
        return kwargs


    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(UpdateWalletView, self).form_valid(form)


class DeleteWalletView(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy('wallet:wallet_list')

    def get_queryset(self):
        return Wallet.objects.filter(owner=self.request.user)

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(DeleteWalletView, self).form_valid(form)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
