from django.contrib import admin
from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import MyappConfig
from catalog.views import (
    CategoryCreateView,
    CategoryDetailView,
    ContactView,
    HomeView,
    ProductCreateView,
    ProductDeleteView,
    ProductDetailView,
    ProductListView,
    ProductTogglePublishView,
    ProductUpdateView,
)

app_name = MyappConfig.name

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("contacts/", ContactView.as_view(), name="contacts"),
    path("products/", cache_page(60 * 5)(ProductListView.as_view()), name="products"),
    path("category/<int:pk>", CategoryDetailView.as_view(), name="category_detail"),
    path("products/create", ProductCreateView.as_view(), name="product_create"),
    path(
        "products/create_category", CategoryCreateView.as_view(), name="category_create"
    ),
    path("products/<int:pk>", ProductDetailView.as_view(), name="product_detail"),
    path(
        "products/<int:pk>/update", ProductUpdateView.as_view(), name="product_update"
    ),
    path(
        "products/<int:pk>/delete", ProductDeleteView.as_view(), name="product_delete"
    ),
    path(
        "product/<int:pk>/toggle-publish/",
        ProductTogglePublishView.as_view(),
        name="product_toggle_publish",
    ),
]
