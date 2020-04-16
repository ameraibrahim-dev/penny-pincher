from django.db import models


class EmailLowerField(models.EmailField):
    def to_python(self, value):
        return value.lower()