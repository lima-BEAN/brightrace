from django.forms import ModelForm
from productapp.models import Product

from django import forms

class ProductForm(forms.ModelForm):
    photo = forms.FileField()
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category', 'photo']
