# Generated by Django 3.0.5 on 2020-05-10 11:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('goal', '0006_auto_20200424_0258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goaltransaction',
            name='is_expense',
            field=models.BooleanField(choices=[(True, 'Expense'), (False, 'Earning')]),
        ),
    ]
