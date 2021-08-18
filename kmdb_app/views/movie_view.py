from rest_framework import status, viewsets
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.serializers import Serializer

from ..models import Movies
from ..serializers import MoviesSerializer
from ..services import movie_genre_service


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        import ipdb

        ipdb.set_trace()
        serializer.is_valid(raise_exception=True)
        # self.perform_create(serializer)
        retrieve_data = movie_genre_service(serializer)
        # serializer.validated_data.pop('genres')
        # movie_data = Movies.objects.get_or_create(**serializer.validated_data)[0]
        # movie_data.genres.set(genres)
        # import ipdb

        # ipdb.set_trace()
        # retrieve_data_serialized = self.get_serializer(data=retrieve_data)
        import ipdb

        ipdb.set_trace()
        return Response(retrieve_data, status=status.HTTP_201_CREATED)
