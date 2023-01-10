from django.contrib import admin
from .models import *

class FoodAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'price',
        'category',
        'image_tag',
    ]

    list_filter = [
        'category__name',
    ]



admin.site.register(Category)
admin.site.register(Food, FoodAdmin)