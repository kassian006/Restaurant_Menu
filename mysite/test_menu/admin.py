from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin


class ExtrasInline(admin.TabularInline):
    model = Extras
    extra = 1


class DrinksInline(admin.TabularInline):
    model = Drinks
    extra = 1


@admin.register(FullMainMenu)
class ProductAdmin(TranslationAdmin):
    inlines = [ExtrasInline, DrinksInline]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class BestSellerImageInline(admin.TabularInline):
    model = BestSellerImage
    extra = 1


@admin.register(BestSellers)
class ProductAdmin(TranslationAdmin):
    inlines = [BestSellerImageInline]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class ImageAboutUsInline(admin.TabularInline):
    model = ImageAboutUs
    extra = 1


@admin.register(AboutUs)
class ProductAdmin(TranslationAdmin):
    inlines = [ImageAboutUsInline]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(Category)
