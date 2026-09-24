from django.contrib import admin
from django.urls import path

from catalog.apps import MyappConfig
from catalog.views import HomeView, ContactView, ProductListView, \
    ProductDetailView, ProductCreateView, CategoryCreateView, ProductUpdateView, ProductDeleteView

app_name = MyappConfig.name

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("contacts/", ContactView.as_view(), name="contacts"),
    path("products/",ProductListView.as_view(), name="products"),
    path("products/create",ProductCreateView.as_view(), name="product_create"),
    path("products/create_category",CategoryCreateView.as_view(), name="category_create"),
    path("products/<int:pk>", ProductDetailView.as_view(), name="product_detail"),
    path("products/<int:pk>/update", ProductUpdateView.as_view(), name="product_update"),
    path("products/<int:pk>/delete", ProductDeleteView.as_view(), name="product_delete")
]
