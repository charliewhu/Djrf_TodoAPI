from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import TodoViewSet

router = SimpleRouter()
router.register('', TodoViewSet, basename='todos')

urlpatterns = router.urls