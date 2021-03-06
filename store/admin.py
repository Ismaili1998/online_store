from django.contrib import admin
from .models import Product
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
    list_display = ['name','price','is_available','stock','created_at','updated_at']

admin.site.register(Product,ProductAdmin)

