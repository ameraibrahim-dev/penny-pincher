from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from api.serializers import CategorySerializer
from category.models import Category
from category.utils import get_predefined_expenses_categories, get_predefined_earnings_categories


class AllExpenseCategoryJsonList(generics.ListAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        expenses = []
        expenses.extend(Category.objects.filter(owner=self.request.user, is_custom=True, is_expense=True))
        expenses.extend(get_predefined_expenses_categories(self.request.user))
        return expenses


class AllEarningsCategoryJsonList(generics.ListAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        earnings = []
        earnings.extend(Category.objects.filter(owner=self.request.user, is_custom=True, is_expense=False))
        earnings.extend(get_predefined_earnings_categories(self.request.user))
        return earnings

