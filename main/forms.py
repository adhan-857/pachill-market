from django import forms
from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name_1", "name_2", "price", "description"]
        labels = {
            "name_1": "Nama Pembeli",
            "name_2": "Nama Produk",
            "price": "Jumlah Produk",
            "description": "Review Pengalaman Berbelanja",
        }