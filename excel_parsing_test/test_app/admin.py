from django.contrib import admin
from import_export.admin import ExportActionModelAdmin
from .models import Product, ProductVariation

@admin.register(Product)
class ProductAdmin(ExportActionModelAdmin):
    list_display = ('id', 'product_name', 'lowest_price', 'last_updated')

@admin.register(ProductVariation)
class ProductVariationAdmin(ExportActionModelAdmin):
    list_display = ('id', 'product', 'variation_text', 'stock', 'last_updated')
