from rest_framework import viewsets, generics, status
from.models import *
from .serializers import *


class BestSellersViewSet(viewsets.ModelViewSet):
    queryset = BestSellers.objects.all()
    serializer_class = BestSellersSerializer


class MainMenuViewSet(viewsets.ModelViewSet):
    queryset = MainMenu.objects.all()
    serializer_class = MainMenuSerializer
