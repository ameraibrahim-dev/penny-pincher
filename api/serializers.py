from rest_framework import serializers

from category.models import Category
from goal.models import GoalTransaction
from wallet.models import WalletTransaction, Wallet


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
        fields = ['id', 'amount', 'date', 'is_expense', 'note', 'category', 'wallet']


class GoalTransactionSerializer(serializers.ModelSerializer):
    amount = MoneySerializer()

    class Meta:
        model = GoalTransaction
        fields = ['id', 'amount', 'date', 'is_expense', 'note', 'goal']


class WalletSerializer(serializers.ModelSerializer):
    balance = MoneySerializer()

    class Meta:
        model = Wallet
        fields = ['id', 'name', 'balance', 'created', 'updated', 'type']
