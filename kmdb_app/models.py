from django.contrib.auth.models import User
from django.db import models


class Movies(models.Model):
    title = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    premiere = models.DateField()
    classification = models.IntegerField()
    synopsis = models.CharField(max_length=255)


class Genres(models.Model):
    name = models.CharField(max_length=255)
    movies = models.ManyToManyField(Movies, related_name="genres")


class Reviews(models.Model):
    critic = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField()
    review = models.CharField(max_length=255)
    spoilers = models.BooleanField()
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
