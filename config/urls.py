from django.contrib import admin
from django.urls import path
# Importações necessárias
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
]

# Adiciona a rota para os arquivos de mídia em modo de desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)