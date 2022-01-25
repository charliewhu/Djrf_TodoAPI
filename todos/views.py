from rest_framework import viewsets

from todos.models import Todo
from todos.permissions import TodoPermissions
from todos.serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    permission_classes = (TodoPermissions, )
    #queryset           = Todo.objects.all()
    serializer_class   = TodoSerializer

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user).order_by('-id')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    