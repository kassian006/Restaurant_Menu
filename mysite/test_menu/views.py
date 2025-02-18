from rest_framework import viewsets, generics
from .serializers import *

class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer


class BestSellersAPIView(generics.ListAPIView):
    queryset = BestSellers.objects.all()
    serializer_class = BestSellersSerializer



class AboutUsAPIView(generics.ListAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer


class FullMainMenuListAPIView(generics.ListAPIView):
    queryset = FullMainMenu.objects.all()
    serializer_class = FullMainMenuListSerializer


class FullMainMenuSimpleAPIView(generics.ListAPIView):
    queryset = FullMainMenu.objects.all()
    serializer_class = FullMainMenuSimpleSerializer


class ExtrasViewSet(viewsets.ModelViewSet):
    queryset = Extras.objects.all()
    serializer_class = ExtrasSerializer


class DrinksViewSet(viewsets.ModelViewSet):
    queryset = Drinks.objects.all()
    serializer_class = DrinkSerializer


class FullMainMenuDetailAPIView(generics.RetrieveAPIView):
    queryset = FullMainMenu.objects.all()
    serializer_class = FullMainMenuDetailSerializer
