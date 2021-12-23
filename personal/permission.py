from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.views import APIView


# class IsOwnerOrReadOnly(BasePermission):
#     def has_permission(self, request, view):
#         if request.method in SAFE_METHODS:
#             return True
#         return request.user.user_type == 'user'

class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # if request.method in permissions.SAFE_METHODS:
        #     return True
        # return request.user.user_type == 'user'
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated and obj.author == request.user
        )