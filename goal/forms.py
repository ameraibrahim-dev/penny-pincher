from django.forms import ModelForm

from goal.models import Goal


class CreateGoalForm(ModelForm):
    class Meta:
        model = Goal
        fields = ['name', 'balance', 'target_amount','target_date']
        labels = {
            'What is the name of your goal': 'name',
            'How much do you want to save': 'target_amount',
            'balance': 'Initial Amount',
            'Ending Date': 'target_date',
        }