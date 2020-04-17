from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from wallet.models import WalletTransaction, Wallet


class CreateTransaction(LoginRequiredMixin, View):
    template_name = 'wallet_transaction/create_transaction.html'
    success_url = reverse_lazy('wallet:wallet_list')
    context = {}

    def get(self, request, wallet_pk=None, *args, **kwargs):
        self.context['wallet'] = Wallet.objects.get(pk=wallet_pk,owner=request.user)
        return render(request, self.template_name, context=self.context)

    def post(self, request, wallet_pk=None, *args, **kwargs):
        print(wallet_pk)
        return HttpResponseRedirect(self.success_url)
