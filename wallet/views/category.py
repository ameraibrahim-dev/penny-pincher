from django.shortcuts import render
from django.views.generic import ListView

from wallet.models import Category
from wallet.utils import get_predefined_expenses_categories, get_predefined_earnings_categories


class CustomCategoryListView(ListView):
    paginate_by = 30

    def get_queryset(self):
        return Category.objects.filter(owner=self.request.user, is_custom=False)


class DefinedExpensesCategories(ListView):
    paginate_by = 30

    def get_queryset(self):
        return get_predefined_expenses_categories(self.user)


class DefinedEarningsCategories(ListView):
    paginate_by = 30

    def get_queryset(self):
        return get_predefined_earnings_categories(self.user)
