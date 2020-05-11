from wallet.models import Category


def get_predefined_expenses_categories(user):
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
    for icon, name in PREDEFINED_EXPENSES_CATEGORIES:
        category = Category.objects.filter(**params, icon=icon, name=name).first()
        if category:
            out.append(category)
        else:
            out.append(Category(name=name, icon=icon, **params))

    return out


def get_predefined_earnings_categories(user):
    out = []
    params = {'is_custom': False, 'is_expense': False, 'owner': user}
    PREDEFINED_EARNINGS_CATEGORIES = [
        ('salary.png', 'Salary'),
        ('business.png', 'Business'),
        ('gifts.png', 'Gifts'),
        ('extra-income.png', 'Extra Income'),
        ('loan.png', 'Loan'),
        ('parental-leave.png', 'Parental Leave'),
        ('insurance.png', 'Insurance'),
    ]
    for icon, name in PREDEFINED_EARNINGS_CATEGORIES:
        category = Category.objects.filter(**params, icon=icon, name=name).first()
        if category:
            out.append(category)
        else:
            out.append(Category(name=name, icon=icon, **params))

    return out
