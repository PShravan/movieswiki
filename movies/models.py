from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone

from django.contrib.auth.models import User


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    genre = models.ManyToManyField(Genre)
    popularity99_rating = models.FloatField(
        verbose_name=u"99Popularity Rating",
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        default=0.0,
        null=True,
    )
    imdb_rating = models.FloatField(
        verbose_name=u"IMDB Rating",
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        default=0.0,
        null=True,
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title