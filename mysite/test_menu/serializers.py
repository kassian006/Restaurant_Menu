from rest_framework import serializers
from .models import *

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name']


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']


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
        fields = ['best_seller_image']


class FullMainMenuListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FullMainMenu
        fields = ['title', 'description', 'price', 'image_menu']


class FullMainMenuSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = FullMainMenu
        fields = ['title', 'description', 'price']


class ExtrasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extras
        fields = ['title', 'price',]


class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extras
        fields = ['title', 'price',]


class FullMainMenuDetailSerializer(serializers.ModelSerializer):
    extras = ExtrasSerializer(read_only=True)
    drink = DrinkSerializer(read_only=True)
    class Meta:
        model = FullMainMenu
        fields = ['title', 'description', 'price', 'image_menu']

