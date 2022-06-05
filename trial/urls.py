from django.urls import path 
from . import views 


urlpatterns = [
    path("contact-us/",views.contact, name="contact"),
    path("free-trial", views.trial, name = "free-trial")
]

