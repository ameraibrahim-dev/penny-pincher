from django.core.exceptions import ValidationError

def MoneyMinValidator(value):
    print(value)
    print(type(value))
    if value<0.00:
        raise ValidationError('This field must equal or grater than {}'.format(min))
    return min
