from decimal import Decimal

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


# Tax Inclusive Pricing Task
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def calculate_tax(self):
        return self.price * Decimal('0.08')

    def calculate_shipping_cost(self, weight: Decimal):
        return weight * Decimal('2.00')

    def format_product_name(self):
        return f'Product: {self.name}'


class DiscountedProduct(Product):
    class Meta:
        proxy = True

    def calculate_price_without_discount(self):
        price_without_discount = Decimal('0.20') * self.price + self.price
        return price_without_discount

    def calculate_tax(self):
        return self.price * Decimal('0.05')

    def calculate_shipping_cost(self, weight: Decimal):
        return weight * Decimal('1.50')

    def format_product_name(self):
        return f"Discounted Product: {self.name}"


# Superhero Universe
class RechargeEnergyMixin:
    def recharge_energy(self, amount: int):
        self.energy = min(self.energy + amount, 100)
        self.save()


class Hero(RechargeEnergyMixin, models.Model):
    name = models.CharField(
        max_length=100
    )
    hero_title = models.CharField(
        max_length=100,
    )
    energy = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1)
        ]
    )


class SpiderHero(Hero):
    def swing_from_buildings(self):
        if self.energy < 80:
            return f"{self.name} as Spider Hero is out of web shooter fluid"

        self.energy = max(self.energy - 80, 1)
        self.save()
        return f"{self.name} as Spider Hero swings from buildings using web shooters"

    class Meta:
        proxy = True


class FlashHero(Hero):
    def run_at_super_speed(self):
        if self.energy < 65:
            return f"{self.name} as Flash Hero needs to recharge the speed force"

        self.energy = max(self.energy - 65, 1)
        self.save()
        return f"{self.name} as Flash Hero runs at lightning speed, saving the day"

    class Meta:
        proxy = True
