from django.db import models
from djmoney.models.fields import MoneyField
from datetime import date

from djmoney.models.validators import MinMoneyValidator
from moneyed import Money

from penny_pincher.models import AbstractTransaction
from user.models import User
from decimal import Decimal


class Goal(models.Model):
    name = models.CharField(max_length=500)
    balance = MoneyField(max_digits=14, decimal_places=2, default_currency='PHP',
                         validators=[MinMoneyValidator(0)])
    target_amount = MoneyField(max_digits=14, decimal_places=2, default_currency='PHP',
                               validators=[MinMoneyValidator(1)])
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    target_date = models.DateField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def saving_progress(self):
        progress = Decimal(self.balance / self.target_amount)
        print(progress)
        progress = round(progress*100, 2)
        print(progress)
        return progress if progress < 100 else 100


class GoalTransaction(AbstractTransaction):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
