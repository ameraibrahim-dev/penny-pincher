from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from api.serializers import CategorySerializer, WalletTransactionSerializer, GoalTransactionSerializer
from category.models import Category
from category.utils import get_predefined_expenses_categories, get_predefined_earnings_categories
from goal.models import GoalTransaction
from wallet.models import WalletTransaction


class AllUsedCategoryJsonList(generics.ListAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Category.objects.filter(owner=self.request.user,wallettransaction__isnull=False).distinct()


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


class WalletTransactionsByUser(generics.ListAPIView):
    serializer_class = WalletTransactionSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['id', 'amount', 'date', 'is_expense', 'note', 'category', 'wallet']

    def get_queryset(self):
        return WalletTransaction.objects.filter(wallet__owner=self.request.user)


class GoalTransactionsByUser(generics.ListAPIView):
    serializer_class = GoalTransactionSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['id', 'amount', 'date', 'is_expense', 'note', 'goal']

    def get_queryset(self):
        return GoalTransaction.objects.filter(goal__owner=self.request.user)
