from rest_framework import status, viewsets
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.serializers import Serializer

from ..models import Movies
from ..serializers import MoviesSerializer
from ..services import movie_genre_post_service


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        retrieve_data = movie_genre_post_service(serializer)
        return Response(retrieve_data, status=status.HTTP_201_CREATED)
