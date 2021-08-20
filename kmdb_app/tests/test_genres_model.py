from django.test import TestCase

from ..models import Genres, Movies


class GenresModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.name = "Ação"
        cls.genre = Genres.objects.create(
            name=cls.name,
        )

    # Verifica se existem os campos da model e a respectiva tipagem
    def test_it_has_information_fields(self):
        self.assertIsInstance(self.genre.name, str)

    def test_str_models_methods(self):
        self.assertEquals(f"<Genres: {self.genre.name}>", str(self.genre))

    def test_it_can_be_attached_to_multiple_movies(self):
        movies = [
            Movies.objects.create(
                title="Um Sonho de Liberdade",
                duration="142m",
                premiere="1994-10-14",
                classification=16,
                synopsis="Andy Dufresne é condenado a duas prisões perpétuas...",
            )
            for _ in range(3)
        ]

        for movie in movies:
            movie.genres.add(self.genre)

        self.assertEquals(len(movies), self.genre.movies.count())
        for movie in movies:
            self.assertIn(movie, list(self.genre.movies.all()))
