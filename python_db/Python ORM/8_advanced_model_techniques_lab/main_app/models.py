from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.

# Rating and Review Content
# Last task
class ReviewMixin(models.Model):
    rating = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(5)
        ]
    )
    review_content = models.TextField()

    class Meta:
        abstract = True
        ordering = ['-rating']



# Restaurant Task
class Restaurant(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(2, message='Name must be at least 2 characters long.'),
            MaxLengthValidator(100, message='Name cannot exceed 100 characters.')
        ]
    )
    location = models.CharField(
        max_length=200,
        validators=[
            MinLengthValidator(2, message="Location must be at least 2 characters long."),
            MaxLengthValidator(200, message="Location cannot exceed 200 characters.")
        ]
    )
    description = models.TextField(
        null=True,
        blank=True
    )
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        validators=[
            MinValueValidator(0.00, message="Rating must be at least 0.00."),
            MaxValueValidator(5.00, message="Rating cannot exceed 5.00.")
        ]
    )


# Menu Task
def validate_menu_categories(value):
    required_categories = [
        'Appetizers',
        'Main Course',
        'Desserts'
    ]
    for category in required_categories:
        if category.lower() not in value.lower():
            raise ValidationError(
                'The menu must include each of the categories "Appetizers", "Main Course", "Desserts".'
            )


class Menu(models.Model):
    name = models.CharField(
        max_length=100,
    )
    description = models.TextField(
        validators=[validate_menu_categories],
    )
    restaurant = models.ForeignKey(to='Restaurant', on_delete=models.CASCADE)


# Restaurant Review Task
class RestaurantReview(ReviewMixin):
    reviewer_name = models.CharField(
        max_length=100,
    )
    restaurant = models.ForeignKey(
        to='Restaurant',
        on_delete=models.CASCADE
    )

    class Meta(ReviewMixin.Meta):
        # abstract=True added for the next task
        abstract = True
        verbose_name = 'Restaurant Review'
        verbose_name_plural = 'Restaurant Reviews'
        unique_together = ['reviewer_name', 'restaurant']


# Restaurant Critic Review Task
class RegularRestaurantReview(RestaurantReview):
    ...


class FoodCriticRestaurantReview(RestaurantReview):
    food_critic_cuisine_area = models.CharField(
        max_length=100
    )

    class Meta(RestaurantReview.Meta):
        verbose_name = 'Food Critic Review'
        verbose_name_plural = 'Food Critic Reviews'


# Menu Review Task
class MenuReview(ReviewMixin):
    reviewer_name = models.CharField(
        max_length=100,
    )
    menu = models.ForeignKey(
        to='Menu',
        on_delete=models.CASCADE
    )

    class Meta(ReviewMixin.Meta):
        verbose_name = 'Menu Review'
        verbose_name_plural = 'Menu Reviews'
        unique_together = ['reviewer_name', 'menu']
        indexes = [
            models.Index(
                fields=['menu'],
                name='main_app_menu_review_menu_id'
            )
        ]
