from django.db import models

from user.models import User


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
