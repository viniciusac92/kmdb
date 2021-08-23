from rest_framework import serializers

from ..models import Reviews
from .user_serializer import UserSerializer


class ReviewsSerializer(serializers.ModelSerializer):
    critic = UserSerializer(default=None)

    class Meta:
        model = Reviews
        fields = ['id', 'critic', 'stars', 'review', 'spoilers']
        extra_kwargs = {'id': {'read_only': True}}

        depth = 1
