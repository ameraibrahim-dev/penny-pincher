from django.db import models
from djmoney.models.fields import MoneyField
from djmoney.models.validators import MinMoneyValidator


class AbstractTransaction(models.Model):
    IS_EXPENSE_CHOICES = [
        (True, 'Expenses'),
        (False, 'Earnings'),
    ]
    amount = MoneyField(max_digits=14, decimal_places=2, default_currency='PHP', validators=[MinMoneyValidator(0.0001)])
    date = models.DateField(null=False, blank=False)
    is_expense = models.BooleanField(null=False, blank=False, choices=IS_EXPENSE_CHOICES)
    note = models.CharField(max_length=3000, null=True, blank=True)

    class Meta:
        abstract = True
