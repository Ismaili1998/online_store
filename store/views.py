from django.shortcuts import render, get_object_or_404
from .models import Product 
from category.models import Category
# Create your views here.


def home(request):
    products = Product.objects.filter(is_available =True)[0:12]
    context = { "products": products }
    return render(request,"home.html",context)

def productDetail(request,category_slug,product_slug):
    product = Product.objects.get(category__slug=category_slug,slug=product_slug)
    context = {"product": product}
    return render(request,"product_detail.html",context)

def store(request, category_slug =None ):
    if category_slug is None : 
        products = Product.objects.filter(is_available=True)
        product_count = products.count()
        context = { "products": products, "product_count":product_count}
        return render(request,"store.html",context)

    category = get_object_or_404(Category,slug=category_slug)
    products = category.product_set.filter(is_available=True)
    product_count = products.count()
    context = {"products":products,"product_count":product_count }
    return render(request,"store.html",context)
