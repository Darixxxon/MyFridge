from django.contrib import admin

from .models import Fridge, Product, FridgeItem, FridgeMembers


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

@admin.register(FridgeItem)
class FridgeItemAdmin(admin.ModelAdmin):
    """
    Admin class for the FridgeItem model.
    """

    list_display = ("fridge", "product", "quantity", "expiration_date")
    search_fields = ("fridge__name", "product__name")
    list_filter = ("fridge",)

@admin.register(FridgeMembers)
class FridgeMembersAdmin(admin.ModelAdmin):
    """
    Admin class for the FridgeMembers model.
    """

    list_display = ("fridge", "member", "role")
    search_fields = ("fridge__name", "member__name")
    list_filter = ("fridge", "member", "role")
