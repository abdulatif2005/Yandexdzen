from rest_framework import permissions


class IsOwnerOrIsStaffOrReadOnly(permissions.BasePermission):
    # Object-level permission to only allow owners of an object to edit it. or if User is staff.

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        return True if obj.user == request.user or request.user.is_staff else False
