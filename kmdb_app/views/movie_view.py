from django.db.models import query
from rest_framework import status, viewsets
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.serializers import Serializer

from ..models import Movies
from ..serializers import MoviesSerializer
from ..services import movie_genre_post_service


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movies.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = MoviesSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        retrieve_data = movie_genre_post_service(serializer)
        return Response(retrieve_data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        if len(request.data) == 0:
            queryset = self.filter_queryset(self.get_queryset())
        else:
            queryset = Movies.objects.filter(title__contains=request.data['title'])

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
