from django.contrib.auth.models import User
from rest_framework import filters, viewsets
from rest_framework.authentication import TokenAuthentication

from ..serializers import UsersSerializer


class AccountViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    # authentication_classes = (TokenAuthentication,)
    # filter_backends = (filters.SearchFilter,)
    # search_fields = (
    #     'username',
    #     'password',
    # )
