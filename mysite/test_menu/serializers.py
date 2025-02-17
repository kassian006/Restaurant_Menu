from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name']


class BestSellersSerializer(serializers.ModelSerializer):
    class Meta:
        model = BestSellers
        fields = ['title', 'description']


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = ['title', 'description']


class BestSellerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BestSellerImage
        fields = ['best_seller']


class FullMainMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = FullMainMenu
        fields = ['title', 'description', 'price', 'image_menu']


class MainMenuSerializer(serializers.ModelSerializer):
    class Meta:
        models = MainMenu
        fields = ['title', 'description', 'price']


class ExtrasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extras
        fields = ['title', 'price',]


class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extras
        fields = ['title', 'price',]
