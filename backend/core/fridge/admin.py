from django.contrib import admin

from .models import Fridge


# Register your models here.
@admin.register(Fridge)
class FridgeAdmin(admin.ModelAdmin):
    """
        Admin class for the Fridge model.
    """

    list_display = ("name", "owner")
    search_fields = ("name", "owner")
    list_filter = ("owner",)
    ordering = ("name",)

