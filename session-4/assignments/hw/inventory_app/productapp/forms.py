from django.forms import ModelForm
from productapp.models import Product

from django import forms

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category']
