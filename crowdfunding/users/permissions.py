from rest_framework import permissions

class IsNotAuthenticated(permissions.BasePermission):
    message = 'You are already logged in.'
    def has_permission(self, request, view):
        return not (request.user.is_authenticated and request.method=="POST")

class IsAuthenticatedAndOwner(permissions.BasePermission):
    message = 'You must be the owner of this object.'
    def has_object_permission(self, request, view, obj):
        if request.method=="GET":
           return False
        if obj.id == request.user:
           return False
        else:
            return True 


class IsOwnerOrReadOnlyUser(permissions.BasePermission):
    message = 'You must be the owner of this object.'
    def has_object_permission(self, request, view, obj):
        if request.method=="GET":
            return True
        return obj.id == request.user.id     
       
    
    

