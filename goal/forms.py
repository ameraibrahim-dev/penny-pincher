from django.forms import ModelForm
from django import forms
from djmoney.forms import MoneyField

from goal.models import Goal, GoalTransaction
from penny_pincher.validators import NotInPastValidator, NotInFutureValidator


class CreateGoalForm(ModelForm):
    target_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}),
                                  validators=[NotInPastValidator])

    class Meta:
        model = Goal
        fields = ['name', 'balance', 'target_amount', 'target_date']
        labels = {
            'name': 'What is the name of your goal',
            'target_amount': 'Target Amount',
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
    target_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}),
                                  validators=[NotInPastValidator])

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
        if self.cleaned_data['balance'].amount > self.cleaned_data['target_amount'].amount:
            self.add_error('target_amount', 'Target amount should grater than or equal your balance')

        return self.cleaned_data


class GoalTransactionForm(ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}),
                                  validators=[NotInFutureValidator])
    class Meta:
        model = GoalTransaction
        fields = ['amount', 'date', 'note', 'is_expense']
        labels = {
            'is_expense': 'Type',
        }
