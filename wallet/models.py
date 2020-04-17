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

    class Meta:
        unique_together = ('name', 'type', 'owner')

    def __str__(self):
        return '{}({})'.format(self.name, self.pk)


class Category(models.Model):
    EXPENSES_ICON_CHOICES = [
        ('food.png', 'food.png'),
        ('shopping.png', 'shopping.png'),
        ('transport.png', 'transport.png'),
        ('home.png', 'home.png'),
        ('bills.png', 'bills.png'),
        ('groceries.png', 'groceries.png'),
        ('health.png', 'health.png'),
        ('entertainment.png', 'entertainment.png'),
    ]
    EARNINGS_ICON_CHOICES = [
        ('salary.png', 'salary.png'),
        ('business.png', 'business.png'),
        ('gifts.png', 'gifts.pn'),
        ('extra-income.png', 'extra-income.png'),
        ('loan.png', 'loan.png'),
        ('parental-leave.png', 'parental-leave.png'),
        ('insurance.png', 'insurance.png'),
    ]
    IS_EXPENSE_CHOICES = [
        (True, 'Expenses'),
        (False, 'Earnings'),
    ]
    name = models.CharField(max_length=500, null=False, blank=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_custom = models.BooleanField(null=False, blank=False)
    is_expense = models.BooleanField(null=False, blank=False, choices=IS_EXPENSE_CHOICES)
    icon = models.CharField(max_length=500, null=False, blank=False,
                            choices=EARNINGS_ICON_CHOICES + EXPENSES_ICON_CHOICES)

    class Meta:
        unique_together = ('name', 'owner')

    def __str__(self):
        return '{}({})'.format(self.name, self.pk)


class WalletTransaction(AbstractTransaction):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)

    def __str__(self):
        return 'WalletTransaction({})'.format(self.pk)
