from django.forms import ModelForm
from django import forms

from user.models import User
from wallet.models import Wallet

class WalletCreateForm(ModelForm):
    user_pk = forms.IntegerField(widget=forms.HiddenInput(), required=True)

    class Meta:
        model = Wallet
        fields = ['name', 'type', 'balance']
        labels = {
            'balance': 'Initial Balance',
        }

    def __init__(self, user=None, *args, **kwargs):
        super(WalletCreateForm, self).__init__(*args, **kwargs)
        self.fields['user_pk'].initial = user.pk

    def clean_balance(self):
        balance = self.cleaned_data.get('balance')
        if balance.amount < 0:
            raise forms.ValidationError('Initial balance must be 0 or grater')
        return balance

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        type = cleaned_data.get('type')
        user_pk = cleaned_data.get('user_pk')
        user = User.objects.get(pk=user_pk)
        if Wallet.objects.filter(owner=user, type=type, name=name):
            raise forms.ValidationError('This wallet is duplicated')


class WalletUpdateForm(ModelForm):
    user_pk = forms.IntegerField(widget=forms.HiddenInput(), required=True)

    class Meta:
        model = Wallet
        fields = ['name', 'type']

    def __init__(self, user=None,pk=None, *args, **kwargs):
        super(WalletUpdateForm, self).__init__(*args, **kwargs)
        self.fields['user_pk'].initial = user.pk

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        type = cleaned_data.get('type')
        user_pk = cleaned_data.get('user_pk')
        user = User.objects.get(pk=user_pk)
        if Wallet.objects.filter(owner=user, type=type, name=name):
            raise forms.ValidationError('This wallet is duplicated')
