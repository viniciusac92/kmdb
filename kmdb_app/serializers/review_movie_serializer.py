from rest_framework import serializers

from ..models import Reviews
from .user_serializer import UserSerializer


class ReviewMovieSerializer(serializers.ModelSerializer):
    critic = UserSerializer(default=None)
    movie = serializers.SlugRelatedField(read_only=True, slug_field='id')

    class Meta:
        model = Reviews
        fields = ['id', 'critic', 'stars', 'review', 'spoilers', 'movie']
        extra_kwargs = {'id': {'read_only': True}}

        depth = 1
