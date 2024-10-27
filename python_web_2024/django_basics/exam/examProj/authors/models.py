from django.core.validators import MinLengthValidator
from django.db import models
from django.db.models import PositiveSmallIntegerField, TextField, URLField

from authors.validators import AlphabeticValidator


class Author(models.Model):
    first_name = models.CharField(
        max_length=40,
        validators=[
            MinLengthValidator(4),
            AlphabeticValidator(),
        ]
    )
    last_name = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(2),
            AlphabeticValidator()
        ]
    )
    passcode = models.CharField(
        max_length=6,
        validators=[
            MinLengthValidator(6, message="Your passcode must be exactly 6 digits!"),
        ],
        help_text="Your passcode must be a combination of 6 digits",
    )
    pets_number = models.PositiveSmallIntegerField(
        null=False,
        blank=False,
    )
    info = models.TextField(
        blank=True,
        null=True,
    )

    image_url = models.URLField(
        blank=True,
        null=True,
    )

