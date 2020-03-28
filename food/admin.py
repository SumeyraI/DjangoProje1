from django.contrib import admin

# Register your models here.
from food.models import Category, Food


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']

class FoodAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'price', 'amount', 'status']
    list_filter = ['status', 'category']

admin.site.register(Category,CategoryAdmin)
admin.site.register(Food,FoodAdmin)
