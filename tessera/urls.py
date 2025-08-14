from django.urls import path
from . import views

app_name = 'tessera'


urlpatterns = [
    # ... suas outras URLs (galeria, etc.)...
    path('dashboard/', views.dashboard, name='dashboard'),

    # Rota para a galeria (já existe)
    path('galeria/', views.galeria, name='galeria'),

    # NOVA ROTA: para os detalhes de uma obra específica
    # <uuid:obra_id> é uma parte dinâmica que vai capturar o ID único da obra
    path('obra/<uuid:id_unico>/', views.detalhe_obra, name='detalhe_obra'),
]