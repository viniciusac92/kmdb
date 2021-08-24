from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from ..models import Reviews
from ..serializers import ReviewMovieSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Reviews.objects.all()
    serializer_class = ReviewMovieSerializer
