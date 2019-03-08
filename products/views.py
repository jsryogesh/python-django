from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
# Create your views here.


def list_products(request):
    products = Product.objects.all()
    return render(request, 'products/products.html', {'products': products})


def create_products(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_products')

    return render(request, 'products/products-form.html', {'form': form})


def update_products(request, id):
    product = Product.objects.get(id=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('list_products')

    return render(request, 'products/products-form.html', {'form': form, 'product': product})


def delete_products(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        product.delete()
        return redirect('list_products')

    return render(request, 'products/products-detele-confirm.html', {'product': product})
