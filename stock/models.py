from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=160)
    sku = models.CharField(max_length=60, unique=True)
    quantity = models.IntegerField(default=0)
    location = models.CharField(max_length=120, blank=True)
    unit_price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.sku})"