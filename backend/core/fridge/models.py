from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Fridge(models.Model):
    """
        Fridge model
        Relationships:
        - Many-to-One with User (Foreign key)
    """

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='fridges',
        related_query_name='fridge',
        null=True,
        blank=True,
        help_text='User who owns the fridge',
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Fridge'
        verbose_name_plural = 'Fridges'

    def __str__(self):
        return f"Fridge {self.name}"
