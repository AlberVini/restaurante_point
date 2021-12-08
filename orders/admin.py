from django.contrib import admin

from .models import Item, Order


class ItemInLine(admin.TabularInline):
    model = Item
    raw_id_fields = ["product"]
    extra = 0


@admin.register(Order)
class OderAdmin(admin.ModelAdmin):
    list_display = ["__str__", "user", "name", "paid", "created", "modified"] 
    list_filter = ["paid", "created", "modified"]
    search_fields = ["name"]
    inlines = [ItemInLine]
