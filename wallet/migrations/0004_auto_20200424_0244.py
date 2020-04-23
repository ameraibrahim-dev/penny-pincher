# Generated by Django 3.0.5 on 2020-04-23 18:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0003_auto_20200423_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallettransaction',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wallettransaction',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
