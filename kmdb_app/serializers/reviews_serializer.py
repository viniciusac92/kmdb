from rest_framework import serializers

from ..models import Reviews


class ReviewsSerializer(serializers.ModelSerializer):
    critic_id = serializers.IntegerField(write_only=True)
    movie_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Reviews
        fields = '__all__'

        depth = 1
