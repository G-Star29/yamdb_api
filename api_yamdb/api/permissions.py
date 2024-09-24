from rest_framework.permissions import BasePermission, SAFE_METHODS


class UserCreate(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST' and request.user.is_anonymous:
            return True


class CategoryCreateOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS or request.user.role == 'admin':
            return True
    def has_object_permission(self, request, view, obj):
        if request.user.role == 'admin':
            return True
