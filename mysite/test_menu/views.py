from rest_framework import viewsets
from .serializers import *

class CategoryListViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class CategoryDetailViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class BestSellersViewSet(viewsets.ModelViewSet):
    queryset = BestSellers.objects.all()
    serializer_class = BestSellersSerializer



class AboutUsViewSet(viewsets.ModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer


class FullMainMenuListViewSet(viewsets.ModelViewSet):
    queryset = FullMainMenu.objects.all()
    serializer_class = FullMainMenuListSerializer


class FullMainMenuSimpleViewSet(viewsets.ModelViewSet):
    queryset = FullMainMenu.objects.all()
    serializer_class = FullMainMenuSimpleSerializer


class ExtrasViewSet(viewsets.ModelViewSet):
    queryset = Extras.objects.all()
    serializer_class = ExtrasSerializer


class DrinksViewSet(viewsets.ModelViewSet):
    queryset = Drinks.objects.all()
    serializer_class = DrinkSerializer


class FullMainMenuDetailViewSet(viewsets.ModelViewSet):
    queryset = FullMainMenu.objects.all()
    serializer_class = FullMainMenuDetailSerializer
