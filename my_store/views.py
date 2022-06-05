
from store.models import Product
from django.shortcuts import render 

def home(request):
    products = Product.objects.filter(is_available =True)[0:9]
    context = { "products": products }
    return render(request,"home.html",context)

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')