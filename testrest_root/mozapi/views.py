from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status  # status code (404, 200...)
from .serializers import TaskSerializer
from .models import Task


#class TaskIdApiView(APIView):
#    serializer_class = TaskSerializer
#
#    # !!! probably we don't need this method in this class
#    def get(self, request, format=None):
#        an_apiview = [
#            "Uses HTTP methods as function (GET, POST, PUT, DELETE)",
#            "It is similar to a traditional Django view",
#            "Gives you the most control over your logic",
#            "Is mapped manually to URLs"
#        ]
#        context = {
#            'message': 'Hello!',
#            'an_apiview': an_apiview
#        } 
#        return Response(context)
#
#    def post(self, request):
#        """Returns task_id
#        """
#        serializer = TaskSerializer(data=request.data)
#        if serializer.is_valid():
#            task_id = serializer.data.get('task_id')
#            message = f"My test string and task id = {task_id}"
#            context = {
#                "message": message,
#                "task_id": task_id
#            }
#            return Response(context)  # response should be task_id
#        else:
#            return Response(
#                serializer.errors,
#                status=status.HTTP_404_BAD_REQUEST
#            )
#
#    def patch(self, request, pk=None):
#        """Patch request, only updates fields provided in the request.
#        """
#        context = {
#            'method': 'patch'
#        }
#        return Response(context)
#
#    def delete(self, request, pk=None):
#        """Delete an object
#        """
#        context = {
#            'method': 'delete'
#        }
#        return Response(context)
#
#
#class HelloViewSet(viewsets.ViewSet):
#    serializer_class = TaskSerializer 
#
#    def list(self, request):
#        a_viewset = [
#            "Uses actions (list, create, retrieve, update, partial_update)",
#            "Automatically maps to URLs using Routers",
#            "Provides more functionality with less code."
#        ] 
#        context = {
#            'message': 'Hello!',
#            'a_viewset': a_viewset
#        }
#        return Response(context)
#
#    def create(self, request):
#        """Responsible for creating a new object in db.
#        """
#        serializer = TaskSerializer(data=request.data)
#        if serializer.is_valid():
#            task_url = serializer.data.get('url')
#            message = f"Hello {task_url}."
#            context = {
#                'message': message
#            }
#            return Response(context)
#        else:
#            return Response(
#                serializer.errors,
#                status=status.HTTP_400_BAD_REQUEST
#            )
#
#    def retrieve(self, request, pk=None):
#        """Handles getting an object by its id.
#        """
#        context = {
#            'http_method': 'GET'
#        }
#        return Response(context)
#
#    def update(self, request, pk=None):
#        """Handles updating an object.
#        """
#        context = {
#            'http_method': "PUT"
#        }
#        return Response(context)
#
#    def partial_update(self, request, pk=None):
#        """Handles updating part of an object.
#        """
#        context = {
#            'http_method': 'PATCH'
#        }
#        return Response(context)
#
#    def destroy(self, request, pk=None):
#        """Handles deleting an object.
#        """
#        context = {
#            'http_method': 'DELETE'
#        }
#        return Response(context)


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()





















class TagsAmountDetailView(APIView):
    pass


# Probably I should add another class for (При GET запиті на  
    # endpoint /tags/<ідентифікатор задачі> вертає
    #підраховану кількість   html тегів які знаходяться на сторінці
    #приклад: {html: 1, head: 1, body: 1. p: 10, img: 2} або помилку якщо url
    #вказує не на html cторінку)


#- При POST запиті на endpoint /tags  з url веб сторінки в якості тіла
#сервіс повертає ідентифікатор задачі
#- При GET запиті на  endpoint /tags/<ідентифікатор задачі> вертає
#підраховану кількість   html тегів які знаходяться на сторінці
#приклад: {html: 1, head: 1, body: 1. p: 10, img: 2} або помилку якщо url
#вказує не на html cторінку
#- При GET запиті на  endpoint /urls/ вертає перелік унікальних url які
#  були надані сервісу
#
