from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from apps.vakanci.models import (
    Vakanci
)
from apps.vakanci.serializer import (
    VacanciiSerializer,
)

class VacanciiView(ModelViewSet):
    queryset= Vakanci.objects.all()
    serializer_class=VacanciiSerializer