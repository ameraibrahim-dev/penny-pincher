from django.forms import ModelForm
from django import forms

from category.utils import get_predefined_expenses_categories, get_predefined_earnings_categories
from user.models import User
from wallet.models import Category


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'icon', 'is_expense']
        labels = {
            'is_expense': 'Type',
        }

