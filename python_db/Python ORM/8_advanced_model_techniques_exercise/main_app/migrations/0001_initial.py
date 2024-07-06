# Generated by Django 5.0.4 on 2024-07-06 08:34

import django.core.validators
import main_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, validators=[django.core.validators.MaxLengthValidator(100), main_app.models.validate_letters_and_spaces])),
                ('age', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(18, 'Age must be greater than or equal to 18')])),
                ('email', models.EmailField(max_length=100, validators=[django.core.validators.EmailValidator(message='Enter a valid email address')])),
                ('phone_number', models.CharField(max_length=10, validators=[django.core.validators.MaxLengthValidator(13), main_app.models.validate_mobile_phone_number])),
                ('website_url', models.URLField(validators=[django.core.validators.URLValidator(message='Enter a valid URL')])),
            ],
        ),
    ]