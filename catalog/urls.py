from django.contrib import admin
from django.urls import path

from catalog.apps import MyappConfig
from catalog.views import HomeView, ContactView, ProductListView, \
    ProductDetailView

app_name = MyappConfig.name

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("contacts/", ContactView.as_view(), name="contacts"),
    path("products/",ProductListView.as_view(), name="products"),
    path("products/<int:pk>", ProductDetailView.as_view(), name="product_detail"),
]
