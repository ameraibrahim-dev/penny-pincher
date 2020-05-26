from datetime import date, datetime
from decimal import Decimal

from django.db import models
from djmoney.models.fields import MoneyField
from djmoney.models.validators import MinMoneyValidator
from djmoney.money import Money

from penny_pincher.models import AbstractTransaction
from user.models import User


class Goal(models.Model):
    name = models.CharField(max_length=500)
    balance = MoneyField(max_digits=14, decimal_places=2, default=Money("0", "PHP"),
                         validators=[MinMoneyValidator(0)])
    target_amount = MoneyField(max_digits=14, decimal_places=2, default_currency='PHP',
                               validators=[MinMoneyValidator(1)])
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    target_date = models.DateField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    opened = models.DateTimeField(null=True)

    @property
    def saving_progress(self):
        progress = Decimal(self.balance / self.target_amount)
        progress = round(progress * 100, 2)
        return progress if progress < 100 else 100

    @property
    def date_progress(self):
        date_interval = self.target_date - self.created.date()
        days_passed = datetime.now().date() - self.created.date()
        progress = Decimal(days_passed / date_interval)
        progress = round(progress * 100, 2)
        return progress if progress < 100 else 100


class GoalTransaction(AbstractTransaction):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
