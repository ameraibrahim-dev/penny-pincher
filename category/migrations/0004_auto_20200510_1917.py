# Generated by Django 3.0.5 on 2020-05-10 11:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('category', '0003_auto_20200510_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='is_expense',
            field=models.BooleanField(choices=[(True, 'Expense'), (False, 'Earning')]),
        ),
    ]
