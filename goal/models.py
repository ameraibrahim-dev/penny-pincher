from django.db import models
from djmoney.models.fields import MoneyField

from penny_pincher.models import AbstractTransaction
from user.models import User


class Goal(models.Model):
    balance = MoneyField(max_digits=14, decimal_places=2, default_currency='PHP')
    progress = models.FloatField(max)
    target_amount = MoneyField(max_digits=14, decimal_places=2, default_currency='PHP')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class GoalTransaction(AbstractTransaction):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
