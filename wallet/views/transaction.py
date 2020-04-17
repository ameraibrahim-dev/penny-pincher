from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from category.models import Category
from category.utils import get_predefined_earnings_categories, get_predefined_expenses_categories
from wallet.forms import WalletTransactionForm
from wallet.models import Wallet, WalletTransaction


class CreateTransactionView(LoginRequiredMixin, CreateView):
    model = WalletTransaction
    form_class = WalletTransactionForm
    template_name = 'wallet_transaction/create_transaction.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        category_name = form.cleaned_data.get('category')
        wallet_pk = self.kwargs.get('pk')
        wallet = Wallet.objects.filter(owner=self.request.user, pk=wallet_pk).first()
        if not wallet:
            raise Http404('wallet not found')
        instance.wallet = wallet
        # modify amount
        if instance.is_expense:
            instance.amount.amount = -instance.amount.amount
        # assign category
        category = Category.objects.filter(name=category_name, is_expense=instance.is_expense).first()

        # if not found,create from predefined
        if not category:
            if instance.is_expense:
                categories = get_predefined_expenses_categories(self.request.user)
            else:
                categories = get_predefined_expenses_categories(self.request.user)
            category = next(filter(lambda x: x.name == category_name, categories))
            category_dict=category.__dict__
            category_dict.pop('_state')
            print(category_dict)
            category = Category.objects.create(**category_dict)

        instance.category = category
        return super(CreateTransactionView, self).form_valid(form)


class OverviewPageCreateTransaction(CreateTransactionView):

    def get_success_url(self):
        return reverse_lazy('wallet:wallet_overview', kwargs={'pk': self.kwargs.get('pk')})


class TransactionPageCreateTransaction(CreateTransactionView):
    def get_success_url(self):
        return reverse_lazy('wallet:wallet_transactions', kwargs={'pk': self.kwargs.get('pk')})
