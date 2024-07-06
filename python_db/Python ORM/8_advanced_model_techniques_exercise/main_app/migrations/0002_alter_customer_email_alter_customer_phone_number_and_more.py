# Generated by Django 5.0.4 on 2024-07-06 08:45

import main_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(error_messages={'invalid': 'Enter a valid email address'}, max_length=254),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(max_length=10, validators=[main_app.models.validate_mobile_phone_number]),
        ),
        migrations.AlterField(
            model_name='customer',
            name='website_url',
            field=models.URLField(error_messages={'invalid': 'Enter a valid URL'}),
        ),
    ]