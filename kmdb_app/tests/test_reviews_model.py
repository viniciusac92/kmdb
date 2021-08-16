from django.contrib.auth.models import User
from django.test import TestCase
from faker import Faker

from ..models import Movies, Reviews

fake = Faker()


class ReviewsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.critic = User.objects.create()
        cls.stars = 16
        cls.review = "O Poderoso Chefão 2 podia ter dado muito certo.."
        cls.spoilers = True
        cls.movie = Movies.objects.create(
            title="Um Sonho de Liberdade",
            duration="142m",
            premiere="1994-10-14",
            classification=16,
            synopsis="Andy Dufresne é condenado a duas prisões perpétuas...",
        )
        cls.review = Reviews.objects.create(
            critic=cls.critic,
            stars=cls.stars,
            review=cls.review,
            spoilers=cls.spoilers,
            movie=cls.movie,
        )

    # Verifica se existem os campos da model e a respectiva tipagem
    def test_it_has_information_fields(self):
        self.assertIsInstance(self.review.critic, object)
        self.assertIsInstance(self.review.stars, int)
        self.assertIsInstance(self.review.review, str)
        self.assertIsInstance(self.review.spoilers, bool)
        self.assertIsInstance(self.review.movie, object)

    def test_str_models_methods(self):
        self.assertEquals(f"<Reviews: {self.review.review}>", str(self.review))

    def test_it_can_be_attached_to_multiple_movies(self):
        critic = User.objects.create(username=fake.first_name())

        movie = Movies.objects.create(
            title=fake.first_name(),
            duration=fake.bothify(text='##m'),
            premiere=fake.date(),
            classification=fake.random_digit(),
            synopsis=fake.text(),
        )

        reviews = [
            Reviews.objects.create(
                critic=critic,
                stars=fake.random_digit(),
                review=fake.text(),
                spoilers=fake.boolean(chance_of_getting_true=50),
                movie=movie,
            )
            for _ in range(3)
        ]

        for rev in reviews:
            self.assertEquals(movie.id, rev.movie.id)

    def test_it_can_be_attached_to_multiple_users(self):

        critic = User.objects.create(username=fake.first_name())

        movie = Movies.objects.create(
            title=fake.first_name(),
            duration=fake.bothify(text='##m'),
            premiere=fake.date(),
            classification=fake.random_digit(),
            synopsis=fake.text(),
        )

        reviews = [
            Reviews.objects.create(
                critic=critic,
                stars=fake.random_digit(),
                review=fake.text(),
                spoilers=fake.boolean(chance_of_getting_true=50),
                movie=movie,
            )
            for _ in range(3)
        ]

        for rev in reviews:
            self.assertEquals(critic.id, rev.critic.id)
