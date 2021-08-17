from rest_framework import serializers

from ..models import Genres


class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = '__all__'
        read_only_fields = ("id",)
        # extra_kwargs = {
        #     'movies': {'many': True},
        # }

        depth = 1
