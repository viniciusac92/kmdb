from rest_framework import serializers

from ..models import Genres


class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = '__all__'

        extra_kwargs = {'movies': {'required': False}}

        # depth = 1
        # def create(self, validated_data):
        #     return super().create(validated_data)
