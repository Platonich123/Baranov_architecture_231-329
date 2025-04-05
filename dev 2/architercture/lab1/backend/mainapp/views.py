from django.shortcuts import render

from django.conf import settings

import rest_framework
from rest_framework import viewsets

from .models import Monowheel
from .serializers import MonowheelSerializer

class MonowheelViewSet(viewsets.ModelViewSet):
    queryset = Monowheel.objects.all()
    serializer_class = MonowheelSerializer