from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from catalog.views import home, contacts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalog.urls', namespace='catalog')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
