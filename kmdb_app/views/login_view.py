from django.contrib.auth.models import User
from rest_framework import viewsets

from ..serializers import UsersSerializer


class LoginViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
