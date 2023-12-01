import datetime
import json
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, HttpResponseNotAllowed
from django.http import JsonResponse
from django.core import serializers
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages  
from main.forms import ProductForm
from .models import Product

# Deploy ulang

@login_required(login_url='/login')
# Create your views here.
def show_main(request):
    products = Product.objects.filter(user=request.user)
    jumlah_total = sum(product.amount for product in products)

    context = {
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

    context = {
        'form': form,
        'name': request.user.username,
        'last_login': request.COOKIES['last_login'],
    }
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

def edit_product(request, id):
    # Get product berdasarkan ID
    product = Product.objects.get(pk = id)

    # Set product sebagai instance dari form
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {
        'form': form,
        'name': request.user.username,
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "edit_product.html", context)

@csrf_exempt
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

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            last_login_time = datetime.datetime.now().replace(microsecond=0)  # Removes microseconds
            formatted_last_login = last_login_time.strftime('%Y-%m-%d %H:%M:%S')  # Formats to string with desired format
            response.set_cookie('last_login', formatted_last_login)
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

def get_product_json(request):
    product_item = Product.objects.all()
    return HttpResponse(serializers.serialize('json', product_item))

@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        name_1 = request.POST.get("name_1")
        price = request.POST.get("price")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        user = request.user

        new_product = Product(name_1=name_1, price=price, amount=amount, description=description, user=user)
        new_product.save()

        jumlah_total = sum(product.amount for product in Product.objects.filter(user=request.user))

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def delete_product_ajax(request):
    if request.method == 'DELETE':
        product_id = request.GET.get('id')  # get id from the query parameter
        try:
            product = Product.objects.get(id=product_id, user=request.user)
            product.delete()
            jumlah_total = sum(product.amount for product in Product.objects.filter(user=request.user))
            return JsonResponse({'status': 'success', 'message': 'Produk berhasil dihapus'}, status=200)
        except Product.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Produk tidak ditemukan'}, status=404)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    else:
        return HttpResponseNotAllowed(['DELETE'])
    
@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # Tambahkan validasi data di sini jika perlu

            new_product = Product.objects.create(
                user = request.user,
                name1 = data.get("name1"), # Pastikan ini sesuai dengan field di model
                price = data.get("price"),
                amount = data.get("amount"),
                description = data.get("description")
            )
            new_product.save()

            return JsonResponse({"status": "success"}, status=200)
        except Exception as e:
            # Tangkap kesalahan dan kirimkan sebagai respons
            return JsonResponse({"status": "error", "message": str(e)}, status=400)
    else:
        return JsonResponse({"status": "error", "message": "Invalid request"}, status=401)