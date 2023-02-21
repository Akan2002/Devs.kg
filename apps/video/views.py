from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from apps.video.serializer import (
    VideoSerializer,
)
from apps.video.models import(
    Video,
)

class VideoView(ModelViewSet):
    queryset= Video.objects.all()
    serializer_class=VideoSerializer
