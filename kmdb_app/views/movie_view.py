from rest_framework import viewsets

from ..models import Movies
from ..serializers import MoviesSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer
