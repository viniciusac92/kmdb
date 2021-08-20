from django.contrib.auth.models import User
from django.db import models

from .movie_model import Movies


class Genres(models.Model):
    name = models.CharField(max_length=255)
    movies = models.ManyToManyField(Movies, related_name="genres")

    def __str__(self) -> str:
        return f"<Genres: {self.name}>"
