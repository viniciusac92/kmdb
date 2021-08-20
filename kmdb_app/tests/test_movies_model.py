from django.test import TestCase
from faker import Faker

from ..models import Genres, Movies

fake = Faker()


class MoviesModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.title = "Um Sonho de Liberdade"
        cls.duration = "142m"
        cls.premiere = "1994-10-14"
        cls.classification = 16
        cls.synopsis = "Andy Dufresne é condenado a duas prisões perpétuas..."
        cls.movie = Movies.objects.create(
            title=cls.title,
            duration=cls.duration,
            premiere=cls.premiere,
            classification=cls.classification,
            synopsis=cls.synopsis,
        )

    # Verifica se existem os campos da model e a respectiva tipagem
    def test_it_has_information_fields(self):
        self.assertIsInstance(self.movie.title, str)
        self.assertIsInstance(self.movie.duration, str)
        self.assertIsInstance(self.movie.premiere, str)
        self.assertIsInstance(self.movie.classification, int)
        self.assertIsInstance(self.movie.synopsis, str)

    def test_str_models_methods(self):
        self.assertEquals(f"<Movies: {self.movie.title}>", str(self.movie))

    def test_it_can_be_attached_to_multiple_genres(self):
        genres = [Genres.objects.create() for _ in range(3)]

        for genre in genres:
            genre.movies.add(self.movie)

        self.assertEquals(len(genres), self.movie.genres.count())
        for genre in genres:
            self.assertIn(genre, list(self.movie.genres.all()))
