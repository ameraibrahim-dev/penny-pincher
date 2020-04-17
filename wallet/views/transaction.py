from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from category.models import Category
from category.utils import get_predefined_expenses_categories
from wallet.models import WalletTransaction


class CreateTransaction(LoginRequiredMixin, View):
    template_name = 'wallet_transaction/create_transaction.html'
    success_url = reverse_lazy('wallet:wallet_list')
    context = {}

    def get(self, request,wallet_pk=None, *args, **kwargs):
        expense_categories = []
        expense_categories.extend(
            Category.objects.filter(owner=self.request.user, is_expense=True, is_custom=True).all())
        expense_categories.extend(get_predefined_expenses_categories(self.request.user))

        self.context['expense_categories']=expense_categories
        return render(request, self.template_name, context=self.context)

    def post(self, request, *args, **kwargs):
        return HttpResponseRedirect(self.success_url)
