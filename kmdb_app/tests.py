from django.test import TestCase

from .models import Genres, Movies

# class MoviesModelTest(TestCase):
#     def test_create_movie_success(self):
#         movie = Movies(
#             title="Um Sonho de Liberdade",
#             duration="142m",
#             premiere="1994-10-14",
#             classification=16,
#             synopsis="Andy Dufresne é condenado a duas prisões perpétuas...",
#         )
#         movie.save()
#         self.assertIsNotNone(movie.id)


class MoviesModel2Test(TestCase):
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

    def test_it_can_be_attached_to_multiple_genres(self):
        genres = [Genres.objects.create() for _ in range(3)]

        for genre in genres:
            genre.movies.add(self.movie)

        self.assertEquals(len(genres), self.movie.genre.count())
        for genre in genres:
            self.assertIn(genre, list(self.movie.genre.all()))