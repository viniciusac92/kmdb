from faker import Faker
from rest_framework import status
from rest_framework.test import APITestCase

from ..models import Movies
from ..serializers import MoviesSerializer

fake = Faker()


class MovieViewsTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.movies = [
            Movies.objects.create(
                title=fake.first_name(),
                duration=fake.bothify(text='##m'),
                premiere=fake.date(),
                classification=fake.random_digit(),
                synopsis=fake.text(),
            )
            for _ in range(3)
        ]
        cls.movie = cls.movies[0]

    def test_can_browse_all_movies(self):
        response = self.client.get(reversed("movies:movie-list"))

        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(len(self.movies), len(response.data))

        for mov in movies:
            self.assertIn(MoviesSerializer(instance=mov).data, response.data)
