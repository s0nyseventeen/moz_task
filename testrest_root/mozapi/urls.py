from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskIdApiView.as_view()),
    # add path for particular "url" like in django detail view
        # it can be <str> type
]
