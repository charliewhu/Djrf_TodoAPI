from rest_framework import viewsets

from todos.models import Todo
from todos.permissions import TodoPermissions
from todos.serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    permissions_class = (TodoPermissions, )
    queryset = Todo.objects.all().order_by('-id')
    serializer_class = TodoSerializer

    