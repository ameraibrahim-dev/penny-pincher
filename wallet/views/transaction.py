from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from category.models import Category
from category.utils import get_predefined_earnings_categories, get_predefined_expenses_categories
from wallet.forms import WalletTransactionForm
from wallet.models import Wallet, WalletTransaction


class CreateTransactionView(LoginRequiredMixin, CreateView):
    model = WalletTransaction
    form_class = WalletTransactionForm
    template_name = 'wallet_transaction/transaction_form.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        category_name = form.cleaned_data.get('category')
        wallet_pk = self.kwargs.get('pk')
        wallet = Wallet.objects.filter(owner=self.request.user, pk=wallet_pk).first()
        if not wallet:
            raise Http404('wallet not found')
        instance.wallet = wallet
        # assign category
        category = Category.objects.filter(name=category_name, is_expense=instance.is_expense).first()

        # if not found,create from pre defined
        if not category:
            if instance.is_expense:
                categories = get_predefined_expenses_categories(self.request.user)
            else:
                categories = get_predefined_earnings_categories(self.request.user)

            category = next(filter(lambda x: x.name == category_name, categories))
            # if category not found in custom / pre defined
            if not category:
                form.add_error('category', 'Invalid Category')
                return self.form_invalid(form)
            # create sand save
            category_dict = category.__dict__
            category_dict.pop('_state')
            category = Category.objects.create(**category_dict)
        # assign category
        instance.category = category
        # update wallet balance
        amount = -instance.amount.amount if instance.is_expense else instance.amount.amount
        instance.wallet.balance.amount += amount
        # if not enough balance
        if instance.wallet.balance.amount < 0:
            form.add_error('amount', 'sufficient Wallet balance')
            return self.form_invalid(form)
        # save wallet balance
        instance.wallet.save()
        return super(CreateTransactionView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Transaction'
        return context


class UpdateTransactionView(LoginRequiredMixin, UpdateView):
    model = WalletTransaction
    form_class = WalletTransactionForm
    template_name = 'wallet_transaction/transaction_form.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        category_name = form.cleaned_data.get('category')
        # reverse wallet_transaction
        original_instance = WalletTransaction.objects.get(pk=instance.pk)
        if original_instance.is_expense:
            instance.wallet.balance.amount += original_instance.amount.amount
        else:
            instance.wallet.balance.amount -= original_instance.amount.amount
        # assign category
        category = Category.objects.filter(name=category_name, is_expense=instance.is_expense).first()

        # if not found,create from pre defined
        if not category:
            if instance.is_expense:
                categories = get_predefined_expenses_categories(self.request.user)
            else:
                categories = get_predefined_earnings_categories(self.request.user)
            category = next(filter(lambda x: x.name == category_name, categories))
            # if category not found in custom / pre defined
            if not category:
                form.add_error('category', 'Invalid Category')
                return self.form_invalid(form)
            # create sand save
            category_dict = category.__dict__
            category_dict.pop('_state')
            category = Category.objects.create(**category_dict)
        # assign category
        instance.category = category
        # update wallet balance
        amount = -instance.amount.amount if instance.is_expense else instance.amount.amount
        instance.wallet.balance.amount += amount
        # if not enough balance
        if instance.wallet.balance.amount < 0:
            form.add_error('amount', 'sufficient Wallet balance')
            return self.form_invalid(form)
            # save wallet balance
        instance.wallet.save()
        return super(UpdateTransactionView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Transaction'
        return context


class DeleteTransactionView(LoginRequiredMixin, DeleteView):

    def get_queryset(self):
        return WalletTransaction.objects.filter(wallet__owner=self.request.user)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.wallet.owner == request.user:
            if self.object.is_expense:
                self.object.wallet.balance.amount += self.object.amount.amount
            else:
                self.object.wallet.balance.amount -= self.object.amount.amount
            self.object.wallet.save()
        return super(DeleteTransactionView, self).delete(request, args, kwargs)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class OverviewPageCreateTransaction(CreateTransactionView):

    def get_success_url(self):
        return reverse_lazy('wallet:wallet_overview', kwargs={'pk': self.kwargs.get('pk')})


class OverviewPageUpdateTransaction(UpdateTransactionView):

    def get_success_url(self):
        return reverse_lazy('wallet:wallet_overview', kwargs={'pk': self.get_object().wallet.pk})


class OverviewPageDeleteTransaction(DeleteTransactionView):

    def get_success_url(self):
        return reverse_lazy('wallet:wallet_overview', kwargs={'pk': self.get_object().wallet.pk})


class TransactionPageCreateTransaction(CreateTransactionView):
    def get_success_url(self):
        return reverse_lazy('wallet:wallet_transactions', kwargs={'pk': self.kwargs.get('pk')})


class TransactionPageUpdateTransaction(UpdateTransactionView):
    def get_success_url(self):
        return reverse_lazy('wallet:wallet_transactions', kwargs={'pk': self.get_object().wallet.pk})


class TransactionPageDeleteTransaction(DeleteTransactionView):
    def get_success_url(self):
        return reverse_lazy('wallet:wallet_transactions', kwargs={'pk': self.get_object().wallet.pk})
