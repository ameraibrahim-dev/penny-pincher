from msilib.schema import ListView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

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
    def get_queryset(self):
        return Wallet.objects.filter(owner=self.request.user)

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.store.owner = self.request.user
        return super(CreateWalletView, self).form_valid(form)


class UpdateWalletView(LoginRequiredMixin, UpdateView):
    def get_queryset(self):
        return Wallet.objects.filter(owner=self.request.user)


def form_valid(self, form):
    instance = form.save(commit=False)
    instance.store.owner = self.request.user
    return super(UpdateWalletView, self).form_valid(form)


class DeleteWalletView(LoginRequiredMixin, DeleteView):
    def get_queryset(self):
        return Wallet.objects.filter(owner=self.request.user)

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.store.owner = self.request.user
        return super(DeleteWalletView, self).form_valid(form)
