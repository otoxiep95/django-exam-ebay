from rest_framework import permissions


class IsOwnerOrNoAccess(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.seller == request.user


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.seller == request.user


class IsCustomerOwnerOrNoAccess(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.buyer == request.user


class IsOwnerOfShoppingCartOrNoAccess(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.shopping_cart.buyer == request.user
