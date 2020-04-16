from django.urls import path, include, reverse_lazy
from .views import CustomCategoryListView, DefinedEarningsCategories, DefinedExpensesCategories

app_name = "wallet"

urlpatterns = [
    # login,logout
    path('custom/category/list', CustomCategoryListView.as_view(), name='custom_categories_list'),
    path('predefined/earnings/category/list', DefinedEarningsCategories.as_view(),
         name='predefined_earnings_categories_list'),
    path('predefined/expenses/category/list', DefinedExpensesCategories.as_view(),
         name='predefined_expenses_categories_list'),
]
