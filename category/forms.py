from django.forms import ModelForm
from django import forms

from category.utils import get_predefined_expenses_categories, get_predefined_earnings_categories
from user.models import User
from wallet.models import Category


class CategoryForm(ModelForm):
    user_pk = forms.IntegerField(widget=forms.HiddenInput(), required=True)

    class Meta:
        model = Category
        fields = ['name', 'icon', 'is_expense']
        labels = {
            'is_expense': 'Type',
        }

    def __init__(self, user=None, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.fields['user_pk'].initial = user.pk

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        user_pk = cleaned_data.get('user_pk')
        user = User.objects.get(pk=user_pk)
        is_expense = cleaned_data.get('is_expense')
        # check if it is predefined category
        if is_expense is True:
            categories = get_predefined_expenses_categories(user)
        else:
            categories = get_predefined_earnings_categories(user)

        for cat in categories:
            if cat.name.lower() == name.lower():
                raise forms.ValidationError('This is a predefined category')
