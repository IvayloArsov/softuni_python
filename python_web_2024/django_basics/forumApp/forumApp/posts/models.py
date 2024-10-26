from django.db import models

from forumApp.posts.choices import LanguageChoice
from forumApp.posts.validators import BadLanguageValidator


class Post(models.Model):
    title = models.CharField(
        max_length=100,
    )

    content = models.TextField(
    )

    author = models.CharField(
        max_length=30
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    languages = models.CharField(
        max_length=20,
        choices=LanguageChoice.choices,
        default=LanguageChoice.OTHER,
    )


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    author = models.CharField(
        max_length=100
    )
    content = models.TextField(

    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

