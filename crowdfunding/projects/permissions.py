from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission): 
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS: 
            return True
        return obj.owner==request.user
    
class IsSupporterOrReadOnly(permissions.BasePermission): 
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS: 
            return True
        return obj.supporter==request.user

class IsNotYourProject(permissions.BasePermission): 
    message="You cannot pledge your own project"
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS: 
            return True
        if request.project in request.user.owned_projects:
            return False
        else:
            return True
