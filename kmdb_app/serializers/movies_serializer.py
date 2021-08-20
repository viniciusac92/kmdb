from kmdb_app.serializers.genres_serializer import GenresSerializer
from rest_framework import serializers

from ..models import Movies


class MoviesSerializer(serializers.ModelSerializer):
    genres = GenresSerializer(many=True)

    class Meta:
        model = Movies
        fields = '__all__'

        extra_kwargs = {'id': {'read_only': True}}
