from django.core.validators import MinValueValidator
from django.forms import ModelForm
from django import forms
from djmoney.forms import MoneyField

from wallet.models import Wallet, WalletTransaction


class WalletCreateForm(ModelForm):
    balance = MoneyField(label='Initial Balance')

    class Meta:
        model = Wallet
        fields = ['name', 'type', 'balance']

    def clean_balance(self):
        balance = self.cleaned_data.get('balance')
        if balance.amount < 0:
            raise forms.ValidationError('Initial balance must be 0 or grater')
        return balance


class WalletUpdateForm(ModelForm):
    class Meta:
        model = Wallet
        fields = ['name', 'type']


class WalletTransactionForm(ModelForm):
    date = forms.DateField(widget=forms.DateInput)
    note = forms.CharField(widget=forms.Textarea, required=False)
    amount = MoneyField()
    category = forms.CharField(required=False, widget=forms.Select(choices=[]))

    class Meta:
        model = WalletTransaction
        fields = ['amount', 'date', 'note', 'is_expense']
        labels = {
            'is_expense': 'Type',
        }

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount.amount < 0:
            raise forms.ValidationError('Amount must be 0 or grater')
        return amount

