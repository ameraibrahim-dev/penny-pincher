from django.db import models
from django.forms import CharField


class EmailLowerField(models.EmailField):
    def to_python(self, value):
        return value.lower()


class StrippedCharField(CharField):
    def clean(self, value):
        if value is not None:
            value = value.strip()
        return super(StrippedCharField, self).clean(value)