from django.urls import path, include, reverse_lazy
from .views import CustomCategoryListView, DefinedEarningsCategories, DefinedExpensesCategories

app_name = "wallet"

urlpatterns = [
    path('custom/category/list', CustomCategoryListView.as_view(), name='custom_categories_list'),
    path('custom/category/create', CustomCategoryListView.as_view(), name='create_custom_categories'),
    path('custom/category/update', CustomCategoryListView.as_view(), name='update_custom_categories_'),
    path('custom/category/delete', CustomCategoryListView.as_view(), name='delete_custom_categories_list'),
    path('predefined/earnings/category/list', DefinedEarningsCategories.as_view(),
         name='predefined_earnings_categories_list'),
    path('predefined/expenses/category/list', DefinedExpensesCategories.as_view(),
         name='predefined_expenses_categories_list'),
]
