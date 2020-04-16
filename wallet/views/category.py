from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from wallet.models import Category
from wallet.utils import get_predefined_expenses_categories, get_predefined_earnings_categories


class CustomCategoryListView(LoginRequiredMixin,ListView):
    paginate_by = 30

    def get_queryset(self):
        return Category.objects.filter(owner=self.request.user, is_custom=False)


class CreateCategoryListView(LoginRequiredMixin,CreateView):
    model = Category
    fields = ['name']
    success_url = reverse_lazy('wallet:')


class UpdateCategoryListView(LoginRequiredMixin,ListView):
    paginate_by = 30

    def get_queryset(self):
        return Category.objects.filter(owner=self.request.user, is_custom=False)


class DeleteCategoryListView(LoginRequiredMixin,ListView):
    paginate_by = 30

    def get_queryset(self):
        return Category.objects.filter(owner=self.request.user, is_custom=False)


class DefinedExpensesCategories(LoginRequiredMixin,ListView):
    paginate_by = 30

    def get_queryset(self):
        return get_predefined_expenses_categories(self.user)


class DefinedEarningsCategories(LoginRequiredMixin,ListView):
    paginate_by = 30

    def get_queryset(self):
        return get_predefined_earnings_categories(self.user)
