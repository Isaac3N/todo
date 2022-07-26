from django.urls import path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r"api/todos", views.TodoViewSet, "todos")

urlpatterns = [
    router.urls
]
