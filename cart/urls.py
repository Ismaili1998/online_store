from django.urls import path 
from . import views 


urlpatterns = [
    path('', views.cart, name='cart'),
    path('add-cart/<str:product_id>/', views.add_cart, name='add-cart'),
    path('remove-cart/<str:product_id>/<str:cart_item_id>/', views.remove_cart, name='remove-cart'),
    path('remove-cart-item/<str:product_id>/<str:cart_item_id>/', views.remove_cart_item, name='remove-cart-item'),
    path('checkout/', views.checkout, name='checkout'),

]
