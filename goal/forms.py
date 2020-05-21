from django import forms
from django.forms import ModelForm
from djmoney.forms import MoneyField

from goal.models import Goal, GoalTransaction
from penny_pincher.validators import NotInPastValidator, NotInFutureValidator


class CreateGoalForm(ModelForm):
    target_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}),
                                  validators=[NotInPastValidator])

    class Meta:
        model = Goal
        fields = ['name', 'target_amount', 'target_date']
        labels = {
            'name': 'What is the name of your goal',
            'target_date': 'Ending Date',
        }

class UpdateGoalForm(ModelForm):
    balance = MoneyField(disabled=True)
    target_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}),
                                  validators=[NotInPastValidator])

    class Meta:
        model = Goal
        fields = ['name', 'target_amount', 'target_date', 'balance']


class GoalTransactionForm(ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = GoalTransaction
        fields = ['amount', 'date', 'note', 'is_expense']
        labels = {
            'is_expense': 'Type',
        }
