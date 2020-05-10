from django.forms import ModelForm

from wallet.models import Category


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'icon', 'is_expense']
        labels = {
            'is_expense': 'Type',
        }
