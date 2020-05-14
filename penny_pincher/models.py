from django.db import models
from djmoney.models.fields import MoneyField
from djmoney.models.validators import MinMoneyValidator


class AbstractTransaction(models.Model):
    IS_EXPENSE_CHOICES = [
        (True, 'Expense'),
        (False, 'Earning'),
    ]
    amount = MoneyField(max_digits=14, decimal_places=2, default_currency='PHP', validators=[MinMoneyValidator(1)])
    date = models.DateField(null=False, blank=False)
    is_expense = models.BooleanField(null=False, blank=False, choices=IS_EXPENSE_CHOICES)
    note = models.CharField(max_length=3000, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    @property
    def sign(self):
        return '-' if self.is_expense else '+'
