from kmdb_app.serializers.genres_serializer import GenresSerializer
from rest_framework import serializers
from rest_framework.relations import ManyRelatedField

from ..models import Movies
from ..services import movie_genre


class MoviesSerializer(serializers.ModelSerializer):
    genres = GenresSerializer(many=True)

    class Meta:
        model = Movies
        # fields = '__all__'
        fields = [
            'id',
            'title',
            'duration',
            'premiere',
            'classification',
            'synopsis',
            'genres',
        ]

        # extra_kwargs = {'id': {'read_only': True}}

        depth = 1

    def create(self, validated_data):
        import ipdb

        ipdb.set_trace()
        return movie_genre(**validated_data)
