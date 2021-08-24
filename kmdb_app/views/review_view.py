from rest_framework import viewsets

from ..models import Reviews
from ..serializers import ReviewMovieSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewMovieSerializer