from django.contrib import admin
from .models import *

class ExtrasInline(admin.TabularInline):
    model = Extras
    extra = 1


class DrinksInline(admin.TabularInline):
    model = Drinks
    extra = 1


class BestSellerImageInline(admin.TabularInline):
    model = BestSellerImage
    extra = 1


class ImageAboutUsInline(admin.TabularInline):
    model = ImageAboutUs
    extra = 1



admin.site.register(Category)
admin.site.register(AboutUs)
admin.site.register(FullMainMenu)
admin.site.register(BestSellers)
admin.site.register(BestSellerImage)
admin.site.register(MainMenu)