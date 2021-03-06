from django.urls import reverse
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
        response = self.client.get(reverse("kmdb:movies-list"))

        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(len(self.movies), len(response.data))
        for mov in self.movies:
            self.assertIn(MoviesSerializer(instance=mov).data, response.data)

    def test_can_read_a_specific_movies(self):
        response = self.client.get(reverse("kmdb:movies-detail", args=[self.movie.id]))

        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(MoviesSerializer(instance=self.movie).data, response.data)
