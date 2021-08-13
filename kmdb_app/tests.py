from django.test import TestCase

from .models import Movies


class MoviesModelTest(TestCase):
    def test_create_movie_success(self):
        movie = Movies(
            title="Um Sonho de Liberdade",
            duration="142m",
            premiere="1994-10-14",
            classification=16,
            synopsis="Andy Dufresne é condenado a duas prisões perpétuas...",
        )
        movie.save()
        self.assertIsNotNone(movie.id)
