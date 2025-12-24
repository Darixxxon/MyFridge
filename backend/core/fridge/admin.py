from django.contrib import admin

from .models import Fridge, Product


# Register your models here.
@admin.register(Fridge)
class FridgeAdmin(admin.ModelAdmin):
    """
    Admin class for the Fridge model.
    """

    list_display = ("name", "owner")
    search_fields = ("name", "owner__username")
    list_filter = ("owner",)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Admin class for the Product model.
    """

    list_display = ("name", "brand", "measurement", "unit", "barcode")
    search_fields = ("name", "brand", "barcode")
    list_filter = ("brand",)
