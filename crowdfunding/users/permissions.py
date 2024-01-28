from rest_framework import permissions

class IsNotAuthenticated(permissions.BasePermission):
    message = 'You are already logged in.'
    def has_permission(self, request, view):
        return not request.user.is_authenticated()
    

class IsAuthenticatedAndOwner(permissions.BasePermission):
    message = 'You must be the owner of this object.'
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user   

