from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core import serializers
from django.urls import reverse
from main.forms import ProductForm
from .models import Product

# Create your views here.
def show_main(request):
    products = Product.objects.all()
    jumlah_total = sum(product.price for product in products)

    context = {
        # Kategori 1
        'kategori_1': 'Makanan',
        # Barang 1 (Kategori 1)
        'barang1_kategori1': 'Roti', # Nama
        'stok1_kategori1': '40', # Jumlah stok
        'harga1_kategori1': '6.000', # Harga
        # Barang 2 (Kategori 1)
        'barang2_kategori1': 'Mie instan', # Nama
        'stok2_kategori1': '65', # Jumlah stok
        'harga2_kategori1': '3.000', # Harga

        # Kategori 2
        'kategori_2': 'Minuman',
        # Barang 1 (Kategori 2)
        'barang1_kategori2': 'Air mineral', # Nama
        'stok1_kategori2': '75', # Jumlah stok
        'harga1_kategori2': '3.500', # Harga
        # Barang 2 (Kategori 2)
        'barang2_kategori2': 'Susu kotak', # Nama
        'stok2_kategori2': '50', # Jumlah stok
        'harga2_kategori2': '7.500', # Harga

        # Kategori 3
        'kategori_3': 'Alat Tulis',
        # Barang 1 (Kategori 2)
        'barang1_kategori3': 'Pulpen gel', # Nama
        'stok1_kategori3': '50', # Jumlah stok
        'harga1_kategori3': '6.500', # Harga
        # Barang 2 (Kategori 2)
        'barang2_kategori3': 'Buku tulis', # Nama
        'stok2_kategori3': '20', # Jumlah stok
        'harga2_kategori3': '5.500', # Harga

        # Nama yang membuat update terakhir
        'nama_updater': 'Ramadhan Andika Putra',

        'jumlah_total': jumlah_total,
        'products': products
    }

    return render(request, "main.html", context)

def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            # Set a default value for the 'amount' field
            product = form.save(commit=False)
            product.amount = 0  # Set the default value
            product.save()
            return redirect('main:show_main')

    else:
        form = ProductForm()

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")