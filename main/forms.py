from django import forms
from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name_1", "price", "amount", "description"]
        labels = {
            "name_1": "Nama Produk",
            "price": "Harga Produk",
            "amount": "Jumlah Produk",
            "description": "Deskripsi Produk",
        }