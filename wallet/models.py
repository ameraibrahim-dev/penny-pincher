from django.db import models
from djmoney.models.fields import MoneyField

from penny_pincher.models import AbstractTransaction
from user.models import User


class Wallet(models.Model):
    TYPE_CHOICES = [
        ('CH', 'Cash'),
        ('EM', 'E-Money'),
        ('CC', 'Credit Card'),
        ('DC', 'Debit Card'),
    ]
    name = models.CharField(max_length=500, null=False, blank=False)
    type = models.CharField(max_length=500, null=False, blank=False, choices=TYPE_CHOICES)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = MoneyField(max_digits=14, decimal_places=2, default_currency='PHP')


class Category(models.Model):
    EXPENSES_ICON_CHOICES = [
        ('CH', 'Health'),
        ('EM', 'E-Money'),
        ('CC', 'Credit Card'),
        ('DC', 'Debit Card'),
    ]
    EARNINGS_ICON_CHOICES = [
        ('CH', 'Cash'),
        ('EM', 'E-Money'),
        ('CC', 'Credit Card'),
        ('DC', 'Debit Card'),
    ]
    IS_EXPENSE_CHOICES = [
        (True, 'Expenses'),
        (False, 'Earnings'),
    ]
    name = models.CharField(max_length=500, null=False, blank=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_custom = models.BooleanField(null=False, blank=False)
    is_Expense = models.BooleanField(null=False, blank=False,choices=IS_EXPENSE_CHOICES)
    icon = models.CharField(max_length=500, null=False, blank=False,
                            choices=EARNINGS_ICON_CHOICES + EXPENSES_ICON_CHOICES)


class WalletTransaction(AbstractTransaction):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
