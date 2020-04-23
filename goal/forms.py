from django.forms import ModelForm
from django import forms
from djmoney.forms import MoneyField

from goal.models import Goal
from penny_pincher.validators import NotInPastValidator


class CreateGoalForm(ModelForm):
    target_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}),
                                  validators=[NotInPastValidator])

    class Meta:
        model = Goal
        fields = ['name', 'balance', 'target_amount', 'target_date']
        labels = {
            'name': 'What is the name of your goal',
            'target_amount': 'target_amount',
            'balance': 'Initial Amount',
            'target_date': 'Ending Date',
        }

    def clean(self):
        if self.cleaned_data['balance'] >= self.cleaned_data['target_amount']:
            self.add_error('target_amount', 'Target amount should grater than your initial amount')
            self.add_error('balance', 'Initial amount should less than your target amount')

        return self.cleaned_data


class UpdateGoalForm(ModelForm):
    balance = MoneyField(disabled=True)

    class Meta:
        model = Goal
        fields = ['name', 'target_amount', 'target_date', 'balance']
        labels = {
            'What is the name of your goal': 'name',
            'How much do you want to save': 'target_amount',
            'Ending Date': 'target_date',
        }

    def clean(self):
        # balance and target amount comparison
        if self.cleaned_data['balance'] >= self.cleaned_data['target_amount']:
            self.add_error('target_amount', 'Target amount should grater than your balance')

        return self.cleaned_data
