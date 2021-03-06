import datetime

from django.core.exceptions import ValidationError


def NotInPastValidator(value):
    today = datetime.datetime.today()
    tomorrow = (today + datetime.timedelta(1)).date()
    if value < tomorrow:
        raise ValidationError('date should be at least {}'.format(tomorrow))


def NotInFutureValidator(value):
    today = datetime.datetime.today().date()
    if value > today:
        raise ValidationError('date should not be over  {}'.format(today))
