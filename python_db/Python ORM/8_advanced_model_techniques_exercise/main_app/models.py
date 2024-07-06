from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator, MinValueValidator, EmailValidator, URLValidator
from django.db import models


# Create your models here.
# Customer Task
def validate_letters_and_spaces(value):
    if not all(char.isalpha() or char.isspace() for char in value):
        raise ValidationError('Name can only contain letters and spaces')


def validate_mobile_phone_number(value: str):
    if not (value.startswith('+359') and len(value) == 13 and value[4:].isdigit()):
        raise ValidationError('Phone number must start with \'+359\' followed by 9 digits')


class Customer(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[
            MaxLengthValidator(100),
            validate_letters_and_spaces
        ]
    )
    age = models.PositiveIntegerField(
        validators=[
            MinValueValidator(18, 'Age must be greater than or equal to 18'),
        ]
    )
    email = models.EmailField(
        error_messages={
            'invalid': 'Enter a valid email address'
        }
    )
    phone_number = models.CharField(
        max_length=13,
        validators=[
            validate_mobile_phone_number,
        ]
    )
    website_url = models.URLField(
        error_messages={
            'invalid': 'Enter a valid URL'
        }
    )

# Media task