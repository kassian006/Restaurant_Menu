from rest_framework import viewsets
from .serializers import *

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class AboutUsViewSet(viewsets.ModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer

class FullMainMenuViewSet(viewsets.ModelViewSet):
    queryset = FullMainMenu.objects.all()
    serializer_class = FullMainMenuSerializer

class ExtrasViewSet(viewsets.ModelViewSet):
    queryset = Extras.objects.all()
    serializer_class = ExtrasSerializer
