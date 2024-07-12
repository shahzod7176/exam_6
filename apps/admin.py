
from django.contrib.admin import register, ModelAdmin, StackedInline

from apps.models import Product, ProductImages


@register(ProductImages)
class ProductImagesModelAdmin(ModelAdmin):
    pass


class ProductImagesInline(StackedInline):
    model = ProductImages
    extra = 1
    min_num = 1


@register(Product)
class ProductModelAdmin(ModelAdmin):
    inlines = [ProductImagesInline]
