from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework import routers

router = DefaultRouter()


urlpatterns =[
    path('', include(router.urls)),
    path('categories/', CategoryListAPIView.as_view(), name='category_list'),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),
    path('best_sellers/', BestSellersAPIView.as_view(), name='best_sellers'),
    path('about_us/', AboutUsAPIView.as_view(), name='about_us'),
    path('manu_simple/', FullMainMenuSimpleAPIView.as_view(), name='manu_simple'),
    path('main_manu/', FullMainMenuListAPIView.as_view(), name='main_manu_list'),
    path('main_manu/<int:pk>/', FullMainMenuDetailAPIView.as_view(), name='main_manu_detail'),

]
