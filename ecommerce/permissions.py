from rest_framework import permissions


class IsCreatorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        # Read-only permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed to the author of a post
        return obj.created_by == request.user


class IsUserOrReadOnly(permissions.BasePermission):

    # def has_permission(self, request, view):
    #
    #     # IF THIS IS A LIST VIEW, CHECK ACCESS LEVEL
    #     if view.action == 'list':
    #         return False
    #     else:
    #         return True

    def has_object_permission(self, request, view, obj):
        # Permissions are only allowed to the owner of the snippet
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user
