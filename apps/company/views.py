from django.shortcuts import render

from apps.company.serializers import(
    companySerializer, company
)

from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

class companyView(ModelViewSet):
    queryset = company.objects.all()
    serializer_class = companySerializer
    permission_classes = (permissions.IsAuthenticated, )
    
