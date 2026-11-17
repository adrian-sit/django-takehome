from django.contrib import admin
from .models import Product, Tag

# Register your models here.
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class BookAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "description")
    filter_horizontal = ("tags",)