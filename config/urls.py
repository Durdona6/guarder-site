from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.index.urls')),
    path('about/', include('apps.about.urls')),
    path('service/', include('apps.service.urls')),
    path('guard/', include('apps.guard.urls')),
    path('contact/', include('apps.contact.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)