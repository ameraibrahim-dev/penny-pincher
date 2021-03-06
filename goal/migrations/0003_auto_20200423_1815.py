# Generated by Django 3.0.5 on 2020-04-23 10:15

import djmoney.models.fields
import djmoney.models.validators
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('goal', '0002_auto_20200423_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='balance',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default_currency='PHP', max_digits=14,
                                                   validators=[djmoney.models.validators.MinMoneyValidator(0)]),
        ),
        migrations.AlterField(
            model_name='goal',
            name='target_amount',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default_currency='PHP', max_digits=14,
                                                   validators=[djmoney.models.validators.MinMoneyValidator(1)]),
        ),
    ]
