from django.urls import path, include
from .views import *
from rest_framework import routers


router =routers.DefaultRouter()
router.register(r'best_seller', BestSellersViewSet, basename='best_seller'),
router.register(r'main_menu', MainMenuViewSet, basename='main_menu'),

urlpatterns =[
    path('', include(router.urls)),
]
