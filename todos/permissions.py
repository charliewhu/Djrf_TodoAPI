from rest_framework import permissions


class TodoPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        #check user owns todo item
        return obj.user == request.user