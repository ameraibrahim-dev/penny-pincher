from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import ProtectedError
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView

from category.utils import get_predefined_expenses_categories, get_predefined_earnings_categories
from wallet.models import Category
from .forms import CategoryForm


class CustomCategoryListView(LoginRequiredMixin, ListView):
    template_name = 'category/custom_category_list.html'

    def get_queryset(self):
        return Category.objects.filter(owner=self.request.user, is_custom=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_custom_category_form'] = CategoryForm
        return context


class CreateCustomCategoryView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/custom_category_form.html'
    success_url = reverse_lazy('category:custom_category_list')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        instance.is_custom = True
        name = form.cleaned_data.get('name')
        is_expense = form.cleaned_data.get('is_expense')
        categories = []
        if is_expense is True:
            categories = get_predefined_expenses_categories(self.request.user)
        else:
            categories = get_predefined_earnings_categories(self.request.user)
        for category in categories:
            if category.name.lower() == name.lower():
                form.add_error('name', 'This category is predefined')
                return self.form_invalid(form)
        return super(CreateCustomCategoryView, self).form_valid(form)


class UpdateCustomCategoryView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('category:custom_category_list')
    template_name = 'category/custom_category_form.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        instance.is_custom = True
        name = form.cleaned_data.get('name')
        is_expense = form.cleaned_data.get('is_expense')
        categories = []
        if is_expense is True:
            categories = get_predefined_expenses_categories(self.request.user)
        else:
            categories = get_predefined_earnings_categories(self.request.user)
        for category in categories:
            if category.name.lower() == name.lower():
                form.add_error('name', 'This category is predefined')
                return self.form_invalid(form)
        return super(UpdateCustomCategoryView, self).form_valid(form)

    def get_queryset(self):
        return Category.objects.filter(owner=self.request.user, is_custom=True)



class DeleteCustomCategoryView(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy('category:custom_category_list')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        instance.is_custom = True
        return super(DeleteCustomCategoryView, self).form_valid(form)

    def get_queryset(self):
        return Category.objects.filter(owner=self.request.user, is_custom=True)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            return self.delete(request, *args, **kwargs)
        except ProtectedError:
            template = 'category/custom_category_delete_error.html'
            context = {'error': 'This category is in used, Can not be delete'}
            return render(request, template, context)


class DefinedExpensesCategories(LoginRequiredMixin, TemplateView):
    template_name = 'category/predefined_expenses_category_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = get_predefined_expenses_categories(self.request.user)
        return context


class DefinedEarningsCategories(LoginRequiredMixin, TemplateView):
    template_name = 'category/predefined_earnings_category_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = get_predefined_earnings_categories(self.request.user)
        return context


