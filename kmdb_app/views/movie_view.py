from django.contrib.auth.models import User
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from ..models import Movies, Reviews
from ..permissions import IsAdminOnly, IsCriticOnly
from ..serializers import MoviesSerializer, ReviewsSerializer
from ..services import movie_genre_post_service, review_owner_check_service


class MovieViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes_by_action = {
        'create': [IsAdminOnly],
        'destroy': [IsAdminOnly],
        'review': [IsCriticOnly],
    }
    queryset = Movies.objects.all()
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

    @action(methods=['POST', 'PUT'], detail=True)
    def review(self, request, *args, **kwargs):
        if request.method == 'POST':
            movie = get_object_or_404(Movies, id=kwargs['pk'])
            review_check = Reviews.objects.filter(movie_id=kwargs['pk'])
            if len(review_check) != 0:
                if review_owner_check_service(request, review_check):
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
            review = Reviews(
                critic=critic[0],
                stars=serialized_data['stars'],
                review=serialized_data['review'],
                spoilers=serialized_data['spoilers'],
                movie=movie,
            )
            review.save()
            retrieve_serialized_data = ReviewsSerializer(review)
            return Response(
                retrieve_serialized_data.data, status=status.HTTP_201_CREATED
            )

        if request.method == 'PUT':
            movie = get_object_or_404(Movies, id=kwargs['pk'])
            review = get_object_or_404(
                Reviews, critic_id=request.user.id, movie_id=movie.id
            )
            review.__dict__['stars'] = request.data['stars']
            review.__dict__['review'] = request.data['review']
            review.__dict__['spoilers'] = request.data['spoilers']
            review.save()
            retrieve_review_serialized = ReviewsSerializer(review)
            return Response(
                retrieve_review_serialized.data, status=status.HTTP_201_CREATED
            )

    def get_permissions(self):
        try:
            return [
                permission()
                for permission in self.permission_classes_by_action[self.action]
            ]
        except KeyError:
            return [permission() for permission in self.permission_classes]
