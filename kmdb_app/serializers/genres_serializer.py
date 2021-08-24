from rest_framework import serializers

from ..models import Genres


class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = ['id', 'name']

        depth = 2
