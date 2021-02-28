from django.contrib import admin
from .models import Product, Category, Attr


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Attr)
class AttrAdmin(admin.ModelAdmin):
    list_display = ['ean']

