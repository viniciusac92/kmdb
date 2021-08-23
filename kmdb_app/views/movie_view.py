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
    serializer_class = MoviesSerializer

    # def get_permissions(self, request, *args, **kwargs):
    #     import ipdb

    #     ipdb.set_trace()
    #     if self.action in ['update', 'partial_update', 'destroy', 'list']:
    #         # which is permissions.IsAdminUser
    #         return request.user and request.user.is_staff
    #     elif self.action in ['create']:
    #         # which is permissions.IsAuthenticated
    #         return request.user and request.user.is_authenticated(request.user)
    #     else:
    #         # which is permissions.AllowAny
    #         return True

    def create(self, request, *args, **kwargs):
        permission_classes = (IsAuthenticated,)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        retrieve_data = movie_genre_post_service(serializer)
        return Response(retrieve_data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        import ipdb

        ipdb.set_trace()
        Movies.objects.filter(title__contains='5')
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
