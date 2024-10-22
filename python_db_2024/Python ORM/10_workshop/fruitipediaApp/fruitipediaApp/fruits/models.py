from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models

from fruitipediaApp.fruits.validators import is_alpha_only


# Create your models here.
class Category(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
    )


class Fruit(models.Model):
    name = models.CharField(
        max_length=30,
        validators=[
            MinLengthValidator(2),
            MaxLengthValidator(30),
            is_alpha_only
        ]
    )

    image_url = models.URLField()
    description = models.TextField()
    nutrition = models.TextField()
