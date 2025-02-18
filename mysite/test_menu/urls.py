from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import *
from rest_framework import routers

router = SimpleRouter()

urlpatterns =[
    path('', include(router.urls)),
    path('categories/', CategoryListAPIView.as_view(), name='category_list'),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),
    path('best_sellers/', BestSellersAPIView.as_view(), name='best_sellers'),
    path('about_us/', AboutUsAPIView.as_view(), name='about_us'),
    path('menu_simple/', FullMainMenuSimpleAPIView.as_view(), name='menu_simple'),
    path('main_menu/', FullMainMenuListAPIView.as_view(), name='main_menu_list'),
    path('main_menu/<int:pk>/', FullMainMenuDetailAPIView.as_view(), name='main_menu_detail'),

]
