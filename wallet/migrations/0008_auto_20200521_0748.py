# Generated by Django 3.0.5 on 2020-05-20 23:48

from decimal import Decimal
from django.db import migrations, models
import djmoney.models.fields
import djmoney.models.validators
import penny_pincher.validators


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0007_merge_20200511_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallet',
            name='opened',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='balance',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('0'), max_digits=14, validators=[djmoney.models.validators.MinMoneyValidator(0)]),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='balance_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('PHP', 'Philippine Peso')], default='XYZ', editable=False, max_length=3),
        ),
        migrations.AlterField(
            model_name='wallettransaction',
            name='date',
            field=models.DateField(validators=[penny_pincher.validators.NotInFutureValidator]),
        ),
    ]
