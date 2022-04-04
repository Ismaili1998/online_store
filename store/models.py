from django.db import models
from category.models import Category
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 100,unique=True)
    slug = models.SlugField(max_length=100,unique=True) 
    description = models.TextField(max_length=500,blank=True)
    price = models.IntegerField()
    is_available = models.BooleanField()
    image = models.ImageField(upload_to = 'photos/products')
    stock = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE) 

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.name
    

    def get_url(self):
        return reverse('product-detail', args = [self.category.slug, self.slug])




