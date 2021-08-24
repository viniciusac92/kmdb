from django.db import models


class Movies(models.Model):
    title = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    premiere = models.DateField()
    classification = models.IntegerField()
    synopsis = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"<Movies: {self.title}>"
