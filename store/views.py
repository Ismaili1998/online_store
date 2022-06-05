from django.shortcuts import render, get_object_or_404
from .models import Product 
from category.models import Category
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
# Create your views here.

def product_detail(request,category_slug,product_slug):
    product = Product.objects.get(category__slug=category_slug,slug=product_slug)
    context = {"product": product}
    return render(request,"product_detail.html",context)

def store(request, category_slug =None ):

    if 'keyword' in request.GET:
        key = request.GET.get('keyword')
        products = Product.objects.filter(Q(description__icontains = key) | Q(name__icontains = key)).order_by('-created_at')
        product_count = products.count()
        context = { "products": products, "product_count":product_count}
        return render(request,"store.html",context)

    if category_slug is None : 
        products = Product.objects.filter(is_available=True).order_by('-created_at')
        paginator = Paginator(products,9)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
        context = { "products": paged_products, "product_count":product_count}
        return render(request,"store.html",context)

    category = get_object_or_404(Category,slug=category_slug)
    products = category.product_set.filter(is_available=True).order_by('created_at')
    paginator = Paginator(products,9)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    product_count = products.count()
    context = {"products":paged_products,"product_count":product_count }
    return render(request,"store.html",context)
