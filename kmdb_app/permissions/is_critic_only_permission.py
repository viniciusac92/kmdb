from rest_framework.permissions import BasePermission


class IsCriticOnly(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.is_staff and not user.is_superuser
