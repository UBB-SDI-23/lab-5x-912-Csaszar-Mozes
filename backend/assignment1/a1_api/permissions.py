from rest_framework import permissions

from .models import UserProfile, UserRoles


class IsSafeToView(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return False


class IsCurrentUserOwner(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return request.user.id == obj.user.id


class IsModerator(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        user_profile = UserProfile.objects.get(user=request.user)
        if user_profile.role == UserRoles.MODERATOR:
            return True
        return False


class IsAdministrator(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        user_profile = UserProfile.objects.get(user=request.user)
        if user_profile.role == UserRoles.ADMIN:
            return True
        return False


