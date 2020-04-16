from user.models import User
from wallet.models import Category


def get_predefined_expense_categories(user):
    out = []
    params = {'is_custom': False, 'is_expense': True, 'owner': user}
    PREDEFINED_EXPENSES_CATEGORIES = [
        ('food.png', 'Food & Drinks'),
        ('shopping.png', 'Shopping'),
        ('transport.png', 'Transport'),
        ('home.png', 'Home'),
        ('bills.png', 'Bills & Fees'),
        ('groceries.png', 'Groceries'),
        ('health.png', 'Health'),
        ('entertainment.png', 'Entertainment'),
    ]
    #todo to be continue
