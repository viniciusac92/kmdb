from rest_framework.permissions import BasePermission


class IsAdminOnly(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.is_staff and user.is_superuser
