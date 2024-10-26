from django.core.validators import MinLengthValidator
from django.db import models

from profiles.validators import AlphaNumValidator


# Create your models here.

class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[
            AlphaNumValidator(),
            MinLengthValidator(2)
        ]
    )
    email = models.EmailField()
    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

