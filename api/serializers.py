from djmoney.money import Money
from rest_framework import serializers

from category.models import Category
from wallet.models import WalletTransaction


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'is_custom', 'is_expense', 'icon']


class MoneySerializer(serializers.Serializer):
    amount = serializers.FloatField()
    currency = serializers.CharField()


class WalletTransactionSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    amount = MoneySerializer()

    class Meta:
        model = WalletTransaction
        fields = ['id', 'amount', 'date', 'is_expense', 'note', 'category', ]
