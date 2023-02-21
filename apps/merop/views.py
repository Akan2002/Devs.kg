from django.shortcuts import render

from apps.merop.serializer import (
    EventSerializer, Event
)
from rest_framework.viewsets import ModelViewSet
class EventView(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

