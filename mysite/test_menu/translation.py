from .models import Category, BestSellers, AboutUs, Extras, MainMenu, FullMainMenu
from modeltranslation.translator import TranslationOptions,register

@register(Category)
class ProductTranslationOptions(TranslationOptions):
    fields = ('category_name',)


@register(BestSellers)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(AboutUs)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Extras)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(FullMainMenu)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(MainMenu)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description')