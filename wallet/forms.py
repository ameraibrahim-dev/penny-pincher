from django import forms
from django.forms import ModelForm
from djmoney.forms import MoneyField

from wallet.models import Wallet, WalletTransaction


class WalletCreateForm(ModelForm):
    balance = MoneyField(label='Initial Balance')

    class Meta:
        model = Wallet
        fields = ['name', 'type', 'balance']


class WalletUpdateForm(ModelForm):
    class Meta:
        model = Wallet
        fields = ['name', 'type']


class WalletTransactionForm(ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
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
