from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from wallet.models import Category
from wallet.utils import get_predefined_expenses_categories, get_predefined_earnings_categories


class CustomCategoryListView(LoginRequiredMixin, ListView):
    paginate_by = 30

    def get_queryset(self):
        return Category.objects.filter(owner=self.request.user, is_custom=True)


class CreateCustomCategoryView(LoginRequiredMixin, CreateView):
    model = Category
    success_url = reverse_lazy('wallet:custom_categories_list')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        instance.is_custom = True
        return super(CreateCustomCategoryView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super(CreateCustomCategoryView, self).get_context_data(**kwargs)
        ctx['title'] = 'Create Store'
        return ctx


class UpdateCustomCategoryView(LoginRequiredMixin, UpdateView):
    model = Category
    fields = ['name']
    success_url = reverse_lazy('wallet:custom_categories_list')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        instance.is_custom = True
        return super(UpdateCustomCategoryView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super(UpdateCustomCategoryView, self).get_context_data(**kwargs)
        ctx['title'] = 'Update Store'
        return ctx

    def get_queryset(self):
        return Category.objects.filter(owner=self.request.user, is_custom=True)


class DeleteCustomCategoryView(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy('wallet:custom_categories_list')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        instance.is_custom = True
        return super(DeleteCustomCategoryView, self).form_valid(form)

    def get_queryset(self):
        return Category.objects.filter(owner=self.request.user, is_custom=True)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class DefinedExpensesCategories(LoginRequiredMixin, ListView):
    paginate_by = 30

    def get_queryset(self):
        return get_predefined_expenses_categories(self.request.user)


class DefinedEarningsCategories(LoginRequiredMixin, ListView):
    paginate_by = 30

    def get_queryset(self):
        return get_predefined_earnings_categories(self.request.user)
