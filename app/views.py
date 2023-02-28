from django.shortcuts import render

from app.models.product import Product

# Create your views here.

def index(request):
    return render(request, 'app/base.html')

def products(request):
    all_products = Product.objects.all()
    return render(request, 'app/products.html', {"all_products":all_products})