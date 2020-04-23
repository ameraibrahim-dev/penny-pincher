from django.forms import ModelForm
from django import forms

from goal.models import Goal


class CreateGoalForm(ModelForm):
    target_date=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    class Meta:
        model = Goal
        fields = ['name', 'balance', 'target_amount','target_date']
        labels = {
            'name':'What is the name of your goal',
            'target_amount': 'target_amount',
            'balance': 'Initial Amount',
            'target_date': 'Ending Date',
        }



class UpdateGoalForm(ModelForm):
    class Meta:
        model = Goal
        fields = ['name','target_amount','target_date']
        labels = {
            'What is the name of your goal': 'name',
            'How much do you want to save': 'target_amount',
            'Ending Date': 'target_date',
        }