from django.contrib.auth.models import User
from django.db import models

from .movie_model import Movies


class Reviews(models.Model):
    critic = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField()
    review = models.CharField(max_length=255)
    spoilers = models.BooleanField()
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"<Reviews: {self.review}>"
