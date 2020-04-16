from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView

from wallet.forms import CategoryForm
from wallet.models import Category
from wallet.utils import get_predefined_expenses_categories, get_predefined_earnings_categories


class CustomCategoryListView(LoginRequiredMixin, ListView):

    def get_queryset(self):
        return Category.objects.filter(owner=self.request.user, is_custom=True)


class CreateCustomCategoryView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('wallet:custom_categories_list')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        instance.is_custom = True
        return super(CreateCustomCategoryView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super(CreateCustomCategoryView, self).get_context_data(**kwargs)
        ctx['title'] = 'Create Category'
        return ctx


class UpdateCustomCategoryView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('wallet:custom_categories_list')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        instance.is_custom = True
        return super(UpdateCustomCategoryView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super(UpdateCustomCategoryView, self).get_context_data(**kwargs)
        ctx['title'] = 'Update Category'
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


class DefinedExpensesCategories(LoginRequiredMixin, TemplateView):
    template_name = "wallet/predefined_expenses_category_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = get_predefined_expenses_categories(self.request.user)
        return context


class DefinedEarningsCategories(LoginRequiredMixin, TemplateView):
    template_name = "wallet/predefined_earnings_category_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = get_predefined_earnings_categories(self.request.user)
        return context
