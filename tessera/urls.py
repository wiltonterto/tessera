from django.urls import path
from . import views

app_name = 'tessera'


urlpatterns = [

    path('dashboard/', views.dashboard, name='dashboard'),
    path('galeria/', views.galeria, name='galeria'),
    path('obra/<uuid:id_unico>/', views.detalhe_obra, name='detalhe_obra'),
]
