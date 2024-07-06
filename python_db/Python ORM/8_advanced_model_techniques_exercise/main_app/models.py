from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator, MinValueValidator, EmailValidator, URLValidator, \
    MinLengthValidator
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

class BaseMedia(models.Model):
    title = models.CharField(
        max_length=100,
    )
    description = models.TextField()
    genre = models.CharField(
        max_length=50,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ['-created_at', 'title']


class Book(BaseMedia):
    class Meta(BaseMedia.Meta):
        verbose_name = f'Model Book'
        verbose_name_plural = f'Models of type - Book'

    author = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(5, 'Author must be at least 5 characters long')
        ]
    )
    isbn = models.CharField(
        unique=True,
        max_length=20,
        validators=[
            MinLengthValidator(6, 'ISBN must be at least 6 characters long')
        ]
    )


class Movie(BaseMedia):
    class Meta(BaseMedia.Meta):
        verbose_name = f'Model Movie'
        verbose_name_plural = f'Models of type - Movie'

    director = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(8, 'Director must be at least 8 characters long')
        ]
    )


class Music(BaseMedia):
    class Meta(BaseMedia.Meta):
        verbose_name = f'Model Music'
        verbose_name_plural = f'Models of type - Music'

    artist = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(9, 'Artist must be at least 9 characters long')
        ]
    )
