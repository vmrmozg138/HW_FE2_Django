from django.contrib import admin
from django.urls import path
from catalog.views import home, contacts
from catalog.apps import MyappConfig

app_name = MyappConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
]
