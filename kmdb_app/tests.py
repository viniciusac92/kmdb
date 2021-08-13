from django.contrib.auth.models import User
from django.test import TestCase

from .models import Genres, Movies, Reviews


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


class ReviewsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.stars = 16
        cls.review = "O Poderoso Chefão 2 podia ter dado muito certo.."
        cls.spoilers = True
        cls.review = Reviews.objects.create(
            stars=cls.title,
            review=cls.review,
            spoilers=cls.spoilers,
        )

    # Verifica se existem os campos da model e a respectiva tipagem
    def test_it_has_information_fields(self):
        self.assertIsInstance(self.review.stars, int)
        self.assertIsInstance(self.review.review, str)
        self.assertIsInstance(self.review.spoilers, bool)

    def test_str_models_methods(self):
        self.assertEquals(f"<Reviews: {self.review.review}>", str(self.review))

    def test_it_can_be_attached_to_multiple_genres(self):
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
        users = [User.objects.create() for _ in range(3)]

        for genre in genres:
            genre.movies.add(self.movie)

        self.assertEquals(len(genres), self.movie.genres.count())
        for genre in genres:
            self.assertIn(genre, list(self.movie.genres.all()))
