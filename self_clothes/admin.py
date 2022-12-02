from django.contrib import admin
from django.contrib.admin import ModelAdmin

from self_clothes.models import self_clothes, Category, Review


# Register your models here.


@admin.register(self_clothes)
class SelfClothesAdmin(ModelAdmin):
    list_display = ('name', 'price', 'category')
    exclude = ('slug',)

    def category(self, obj):
        return obj.category_set.first.name


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('name', 'clothes_count')

    def clothes_count(self, obj):
        return obj.self_clothes_set.count()


@admin.register(Review)
class ReviewAdmin(ModelAdmin):
    list_display = ('id', 'text')

    def author(self, obj):
        return obj.user_set.name
