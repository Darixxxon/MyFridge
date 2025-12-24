from decimal import Decimal

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


# Create your models here.

class Fridge(models.Model):
    """
    Fridge model
    Relationships:
    - Many-to-One with User (Foreign key)
    """

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='fridges',
        related_query_name='fridge',
        help_text='User who owns the fridge',
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Fridge'
        verbose_name_plural = 'Fridges'

    def __str__(self):
        return f"Fridge {self.name}"

class Product(models.Model):
    """
    Product model
    """

    UNITS = [
        ("g", "Grams"),
        ("kg", "Kilograms"),
        ("ml", "Milliliters"),
        ("l", "Liters"),
        ("pc", "Piece")
    ]

    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True, default='')
    brand = models.CharField(max_length=100, blank=True, default='')
    measurement = models.DecimalField(decimal_places=2, max_digits=10, validators=[MinValueValidator(Decimal("0.01"))])
    unit = models.CharField(max_length=5, choices=UNITS, blank=False)
    barcode = models.CharField(max_length=13, unique=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f"Product {self.name} with barcode {self.barcode}"
