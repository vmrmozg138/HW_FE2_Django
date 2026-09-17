from django.contrib import admin
from django.urls import path

from catalog.apps import MyappConfig
from catalog.views import contacts, home, products, product_details

app_name = MyappConfig.name

urlpatterns = [
    path("", home, name="home"),
    path("contacts/", contacts, name="contacts"),
    path("products/",products, name="products"),
    path("products/<int:product_id>", product_details, name="product_details"),
]
