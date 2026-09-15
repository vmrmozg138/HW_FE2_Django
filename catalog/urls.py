from django.contrib import admin
from django.urls import path

from catalog.apps import MyappConfig
from catalog.views import contacts, home

app_name = MyappConfig.name

urlpatterns = [
    path("", home, name="home"),
    path("contacts/", contacts, name="contacts"),
]
