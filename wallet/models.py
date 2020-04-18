from django.db import models
from djmoney.models.fields import MoneyField

from category.models import Category
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

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('name', 'type', 'owner')

    def __str__(self):
        return '{}({})'.format(self.name, self.pk)


class WalletTransaction(AbstractTransaction):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)

    def __str__(self):
        return 'WalletTransaction({})'.format(self.pk)
