from django.urls import path, include, reverse_lazy
from .views import *

app_name = "category"

urlpatterns = [
    # categories
    path('custom/list/', CustomCategoryListView.as_view(), name='custom_categories_list'),
    path('custom/create/', CreateCustomCategoryView.as_view(), name='create_custom_categories'),
    path('custom/update/<int:pk>/', UpdateCustomCategoryView.as_view(), name='update_custom_categories'),
    path('custom/delete/<int:pk>/', DeleteCustomCategoryView.as_view(), name='delete_custom_categories_list'),
    path('predefined/earnings/list/', DefinedEarningsCategories.as_view(),
         name='predefined_earnings_categories_list'),
    path('predefined/expenses/list/', DefinedExpensesCategories.as_view(),
         name='predefined_expenses_categories_list'),
    path('expenses/list/json/', AllExpenseCategoryJsonList.as_view(),
         name='all_expenses_json'),
]
