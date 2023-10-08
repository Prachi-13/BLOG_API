from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrSuperuserOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser or request.method in SAFE_METHODS:
            return True
        return obj.author == request.user

class IsUserOrReadOnly(BasePermission):
    """
    Object-level permission to only allow users of an object to edit it.
    Assumes the model instance has an `user` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in SAFE_METHODS:
            return True
        # Instance must have an attribute named `user`.
        return obj == request.user
    

class IsStaffOrUserOrReadOnly(IsUserOrReadOnly):
    """
    Object-level permission to only allow authors and staff members of an object to edit it.
    Assumes the model instance has an `author` and user instance has a `staff` attribute.
    """

    def has_object_permission(self, request, view, obj):
        perms = super().has_object_permission(request, view, obj)
        print("perms", perms)
        return bool(perms or request.user.is_staff)

