from rest_framework import serializers
from .models import *


class BestSellersSerializer(serializers.ModelSerializer):
    class Meta:
        model = BestSellers
        fields = '__all__'


class BestSellerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BestSellerImage
        fields = '__all__'


class MainMenuSerializer(serializers.ModelSerializer):
    class Meta:
        models = MainMenu
        fields = ['title', 'description', 'price']


