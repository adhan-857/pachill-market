import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponseRedirect
from django.http import HttpResponse
from django.core import serializers
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages  
from main.forms import ProductForm
from .models import Product

@login_required(login_url='/login')
# Create your views here.
def show_main(request):
    products = Product.objects.filter(user=request.user)
    jumlah_total = sum(product.amount for product in products)

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
        'nama_updater': 'Ramadhan Andika Putra (2206081976) - PBP A',

        'jumlah_total': jumlah_total,
        'products': products,
        'name': request.user.username,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    else:
        form = ProductForm()

    context = {'form': form}
    return render(request, "create_product.html", context)

def delete_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        product.delete()
        return redirect('main:show_main')
    except Product.DoesNotExist:
        # Handle jika produk tidak ditemukan
        pass

def increase_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        product.amount += 1
        product.save()
        return redirect('main:show_main')
    except Product.DoesNotExist:
        # Handle jika produk tidak ditemukan
        pass

def decrease_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        if product.amount > 0:
            product.amount -= 1
            product.save()
        return redirect('main:show_main')
    except Product.DoesNotExist:
        # Handle jika produk tidak ditemukan
        pass

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun kamu sudah berhasil dibuat!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Maaf, username atau password yang anda berikan salah. Mohon coba lagi! :D')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

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