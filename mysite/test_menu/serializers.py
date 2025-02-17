from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name']


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = ['title', 'description']


class FullMainMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = FullMainMenu
        fields = ['title', 'description', 'price', 'image_menu']


class ExtrasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extras
        fields = ['title', 'price',]