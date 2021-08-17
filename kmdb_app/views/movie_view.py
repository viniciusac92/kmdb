from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView

from ..models import Movies
from ..serializers import MoviesSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer
