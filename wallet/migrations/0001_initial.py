# Generated by Django 3.0.5 on 2020-04-18 05:31

import django.db.models.deletion
import djmoney.models.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('category', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('type', models.CharField(
                    choices=[('CH', 'Cash'), ('EM', 'E-Money'), ('CC', 'Credit Card'), ('DC', 'Debit Card')],
                    max_length=500)),
                ('balance_currency',
                 djmoney.models.fields.CurrencyField(choices=[('PHP', 'Philippine Peso')], default='PHP',
                                                     editable=False, max_length=3)),
                ('balance', djmoney.models.fields.MoneyField(decimal_places=2, default_currency='PHP', max_digits=14)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('name', 'type', 'owner')},
            },
        ),
        migrations.CreateModel(
            name='WalletTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_currency',
                 djmoney.models.fields.CurrencyField(choices=[('PHP', 'Philippine Peso')], default='PHP',
                                                     editable=False, max_length=3)),
                ('amount', djmoney.models.fields.MoneyField(decimal_places=2, default_currency='PHP', max_digits=14)),
                ('date', models.DateField()),
                ('is_expense', models.BooleanField(choices=[(True, 'Expenses'), (False, 'Earnings')])),
                ('note', models.CharField(blank=True, max_length=3000, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='category.Category')),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.Wallet')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
