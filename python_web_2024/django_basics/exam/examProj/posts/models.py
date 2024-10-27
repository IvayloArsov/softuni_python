from uu import Error

from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models


class Post(models.Model):
    title = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(5),
        ],
        unique=True,
    )

    def clean(self):
        if self.pk:
            existing_post = Post.objects.filter(title=self.title).exclude(pk=self.pk)
            if existing_post.exists():
                raise ValidationError("Oops! That title is already taken. How about something fresh and fun?")

        else:
            if Post.objects.filter(title=self.title).exists():
                raise ValidationError("Oops! That title is already taken. How about something fresh and fun?")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    image_url = models.URLField(
        null=False,
        blank=False,
        help_text="Share your funniest furry photo URL!"
    )
    content = models.TextField(
        null=False,
        blank=False,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        editable=False,
    )
    author = models.ForeignKey(
        to='authors.Author',
        on_delete=models.CASCADE,
        editable=False,
        related_name='posts',
    )
