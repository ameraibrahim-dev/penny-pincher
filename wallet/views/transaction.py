from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from wallet.models import Wallet


class CreateTransaction(LoginRequiredMixin, View):
    template_name = 'wallet_transaction/create_transaction.html'
    success_url = reverse_lazy('wallet:wallet_transactions')
    context = {}

    def get(self, request, wallet_pk=None, *args, **kwargs):
        self.context['wallet'] = Wallet.objects.get(pk=wallet_pk, owner=request.user)
        if not self.context.get('wallet'):
            raise Http404("Wallet does not exist")
        return render(request, self.template_name, context=self.context)

    def post(self, request, wallet_pk=None, *args, **kwargs):
        wallet = Wallet.objects.get(pk=wallet_pk, owner=request.user)
        category = self.POST.get('category')
        date = self.POST.get('date')
        note = self.POST.get('note')
        amount = self.POST.get('amount')
        if not wallet:
            raise Http404("Wallet does not exist")

        return HttpResponseRedirect(self.success_url)
