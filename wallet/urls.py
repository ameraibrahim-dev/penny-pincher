from django.urls import path, include, reverse_lazy
from .views import CustomCategoryListView, DefinedExpensesCategories, DefinedEarningsCategories, \
    DeleteCustomCategoryView, UpdateCustomCategoryView, CreateCustomCategoryView

app_name = "wallet"

urlpatterns = [
    # categories
    path('custom/category/list/', CustomCategoryListView.as_view(), name='custom_categories_list'),
    path('custom/category/create/', CreateCustomCategoryView.as_view(), name='create_custom_categories'),
    path('custom/category/update/<int:pk>/', UpdateCustomCategoryView.as_view(), name='update_custom_categories'),
    path('custom/category/delete/<int:pk>/', DeleteCustomCategoryView.as_view(), name='delete_custom_categories_list'),
    path('predefined/earnings/category/list/', DefinedEarningsCategories.as_view(),
         name='predefined_earnings_categories_list'),
    path('predefined/expenses/category/list/', DefinedExpensesCategories.as_view(),
         name='predefined_expenses_categories_list'),
]
