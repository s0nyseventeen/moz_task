from rest_framework import viewsets
from rest_framework.views import APIView
from . import serializers
from . import models


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TaskSerializer
    queryset = models.Task.objects.all()


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
