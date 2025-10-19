from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "sku", "quantity", "location", "unit_price", "is_active", "updated_at")
    list_filter = ("is_active", "updated_at", "location")
    search_fields = ("name", "sku", "location")
    ordering = ("name",)