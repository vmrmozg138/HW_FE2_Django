from django.contrib import admin
from django.urls import path
from myapp.views import hello

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello),  # любой GET на корень отдаст наш ответ
]
