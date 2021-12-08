from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "nome",
        "slug",
        "category",
        "preco",
        "disponivel",
        "restaurante",
    ]

    list_filter = ["disponivel", "restaurante"]
    list_editable = ["preco", "disponivel"]
