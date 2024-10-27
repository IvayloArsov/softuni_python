# Generated by Django 5.0.4 on 2024-07-11 15:08

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_movie_genre_alter_movie_last_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='director',
            name='years_of_experience',
            field=models.SmallIntegerField(default=0, validators=[django.core.validators.MinLengthValidator(0)]),
        ),
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(related_name='actor_movies', to='main_app.actor'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='director_movies', to='main_app.director'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(choices=[('Action', 'Action'), ('Comedy', 'Comedy'), ('Drama', 'Drama'), ('Other', 'Other')], default='Other', max_length=6, validators=[django.core.validators.MaxLengthValidator(6)]),
        ),
        migrations.AlterField(
            model_name='movie',
            name='last_updated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]