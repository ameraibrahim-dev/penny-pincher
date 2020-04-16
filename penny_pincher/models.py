from django.db import models
from djmoney.models.fields import MoneyField


class AbstractTransaction(models.Model):
    amount = MoneyField(max_digits=14, decimal_places=2, default_currency='PHP')
    date = models.DateField()
    isExpense = models.BooleanField(null=False, blank=False)
    note = models.CharField(max_length=3000,null=True,blank=True)

    class Meta:
        abstract = True
