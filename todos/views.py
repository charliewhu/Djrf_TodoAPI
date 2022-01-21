from rest_framework import viewsets

from todos.models import Todo
from todos.permissions import TodoPermissions
from todos.serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    permission_classes = (TodoPermissions, )
    serializer_class   = TodoSerializer

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user)

    