from rest_framework import permissions
from rest_framework.views import APIView


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.user_type == 'user'


    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.user_type == 'user'


class ExampleView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
