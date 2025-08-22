from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from tessera import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tessera/', include('tessera.urls')),
    path('galeria/', views.galeria, name='galeria'),
    path('', views.home, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
