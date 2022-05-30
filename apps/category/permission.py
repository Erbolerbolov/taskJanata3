from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAdminUser


class IsAdminOrAlloAny(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS: #GET OPYION HEAD
            return True
        return bool(request.user and request.user.is_staff)