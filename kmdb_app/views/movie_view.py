from django.contrib.auth.models import User
from rest_framework import serializers, status, viewsets
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.serializers import Serializer

from ..models import Movies, Reviews
from ..serializers import MoviesSerializer, ReviewsSerializer, UserSerializer
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
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['POST'], detail=True)
    def review(self, request, *args, **kwargs):
        movie = get_object_or_404(Movies, id=kwargs['pk'])
        # import ipdb

        # ipdb.set_trace()
        review_check = Reviews.objects.filter(movie_id=kwargs['pk'])
        if (
            len(review_check) != 0
            and review_check[0].__dict__['critic_id'] == request.user.id
        ):
            return Response(
                {'detail': 'You already made this review.'},
                status=status.HTTP_422_UNPROCESSABLE_ENTITY,
            )

        serializer = ReviewsSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                {'detail': 'Serializer inválido.'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serialized_data = serializer.validated_data
        critic = User.objects.filter(id=request.user.id)
        # import ipdb

        # ipdb.set_trace()
        review = Reviews(
            critic=critic[0],
            stars=serialized_data['stars'],
            review=serialized_data['review'],
            spoilers=serialized_data['spoilers'],
            movie=movie,
        )
        # import ipdb

        # ipdb.set_trace()
        review.save()
        import ipdb

        ipdb.set_trace()
        retrieve_serialized_data = ReviewsSerializer(review)

        return Response(retrieve_serialized_data.data, status=status.HTTP_201_CREATED)
