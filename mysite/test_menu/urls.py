from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'aboutus', AboutUsViewSet)
router.register(r'mainmenu', FullMainMenuViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
