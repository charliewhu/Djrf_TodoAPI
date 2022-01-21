from rest_framework import viewsets

from todos.models import Todo
from todos.serializers import TodoSerializer

# Create your views here.
class TodoViewSet(viewsets.ModelViewSet): # new
    queryset = Todo.objects.all().order_by('-id')
    serializer_class = TodoSerializer