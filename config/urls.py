from django.contrib import admin
from django.urls import path, include # Adicione "include" aqui
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Adicione esta linha:
    # Qualquer URL que começar com "tessera/" será enviada para o urls.py do nosso app
    path('tessera/', include('tessera.urls')), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
