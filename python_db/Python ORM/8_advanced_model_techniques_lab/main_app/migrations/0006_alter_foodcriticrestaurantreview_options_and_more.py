# Generated by Django 5.0.4 on 2024-07-06 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_foodcriticrestaurantreview_regularrestaurantreview'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='foodcriticrestaurantreview',
            options={'verbose_name': 'Food Critic Review', 'verbose_name_plural': 'Food Critic Reviews'},
        ),
        migrations.AlterUniqueTogether(
            name='foodcriticrestaurantreview',
            unique_together=set(),
        ),
    ]