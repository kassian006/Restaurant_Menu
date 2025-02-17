from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework import routers

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'aboutus', AboutUsViewSet)
router.register(r'mainmenu', FullMainMenuViewSet)
router.register(r'best_seller', BestSellersViewSet, basename='best_seller'),
router.register(r'main_menu', MainMenuViewSet, basename='main_menu'),

urlpatterns =[
    path('', include(router.urls)),
]
