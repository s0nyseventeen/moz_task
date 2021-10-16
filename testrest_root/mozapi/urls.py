from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

router = DefaultRouter()
router.register('task', TaskViewSet)

urlpatterns = [
    path('', include(router.urls))
    # add path for particular "url" like in django detail view
        # it can be <str> type
]
