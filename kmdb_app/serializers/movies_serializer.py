from drf_writable_nested import WritableNestedModelSerializer
from kmdb_app.serializers.genres_serializer import GenresSerializer
from rest_framework import serializers

from ..models import Movies


class MoviesSerializer(serializers.ModelSerializer):
    genres = GenresSerializer(many=True)

    class Meta:
        model = Movies
        fields = '__all__'
        # fields = [
        #     'id',
        #     'title',
        #     'duration',
        #     'premiere',
        #     'classification',
        #     'synopsis',
        #     'genres',
        # ]

        extra_kwargs = {'id': {'read_only': True}}

        # depth = 1

    # def create(self, validated_data):

    #     return super().create(validated_data)
