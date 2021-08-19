from django.contrib.auth.models import User
from rest_framework import serializers


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'is_superuser',
            'is_staff',
        ]
