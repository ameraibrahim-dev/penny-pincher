# Generated by Django 3.0.5 on 2020-05-10 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_auto_20200418_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='icon',
            field=models.CharField(choices=[('salary.png', 'salary.png'), ('business.png', 'business.png'), ('gifts.png', 'gifts.png'), ('extra-income.png', 'extra-income.png'), ('loan.png', 'loan.png'), ('parental-leave.png', 'parental-leave.png'), ('insurance.png', 'insurance.png'), ('food.png', 'food.png'), ('shopping.png', 'shopping.png'), ('transport.png', 'transport.png'), ('home.png', 'home.png'), ('bills.png', 'bills.png'), ('groceries.png', 'groceries.png'), ('health.png', 'health.png'), ('entertainment.png', 'entertainment.png')], max_length=500),
        ),
    ]