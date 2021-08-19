from django.contrib.auth.models import User
from django.urls import reverse
from faker import Faker
from rest_framework import status
from rest_framework.test import APITestCase

from ..serializers import UsersSerializer

fake = Faker()


class AccountsViewsTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.accounts = [
            User.objects.create(
                username=fake.first_name(),
                first_name=fake.name(),
                last_name=fake.last_name(),
                is_superuser=fake.boolean(chance_of_getting_true=30),
                is_staff=fake.boolean(chance_of_getting_true=30),
            )
            for _ in range(3)
        ]

        cls.account = cls.accounts[0]

    def test_can_browse_all_users(self):
        response = self.client.get(reverse("kmdb:user-list"))

        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(len(self.accounts), len(response.data))
        for acc in self.accounts:
            self.assertIn(UsersSerializer(instance=acc).data, response.data)

    def test_can_read_a_specific_users(self):
        # (5)
        response = self.client.get(reverse("kmdb:user-detail", args=[self.account.id]))

        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(UsersSerializer(instance=self.account).data, response.data)
