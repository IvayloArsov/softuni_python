# Generated by Django 5.0.4 on 2024-07-06 07:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_menureview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodcriticrestaurantreview',
            name='rating',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='regularrestaurantreview',
            name='rating',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(5)]),
        ),
    ]
