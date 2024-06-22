from tasks.apps import TasksConfig
from rest_framework.routers import DefaultRouter

from tasks.views import TaskViewSet

app_name = TasksConfig.name

# Создание роутера и регистрация маршрутов для TaskViewSet
router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='tasks')

# Объединение маршрутов в urlpatterns
urlpatterns = [

              ] + router.urls
