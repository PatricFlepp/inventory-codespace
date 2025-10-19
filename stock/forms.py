from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["name", "sku", "quantity", "location", "unit_price", "is_active"]