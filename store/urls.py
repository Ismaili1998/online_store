from django.urls import path 
from . import views 


urlpatterns = [
    path("",views.store, name="store"),
    path("<slug:category_slug>/<slug:product_slug>/",views.product_detail, name="product-detail"),
    path("<slug:category_slug>/", views.store, name = "products-by-category"),
    path("search", views.store, name = "search")
    #path('submit-review/<str:product_id>/', views.submit_review, name='submit-review'),
]


