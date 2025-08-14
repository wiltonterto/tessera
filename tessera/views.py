# tessera/views.py
from django.shortcuts import render, get_object_or_404
from .models import ObraDeArte, Artista
from django.db.models import Q

def dashboard(request):
    # Por enquanto, esta view apenas renderiza o template.
    # No futuro, vamos buscar dados aqui (ex: obras recentes).
    context = {}
    return render(request, 'tessera/dashboard.html', context)

# View para a página da galeria, com busca por título e artista
def galeria(request):
    termo_busca = request.GET.get('q')
    obras = ObraDeArte.objects.all()

    if termo_busca:
        obras = obras.filter(
            Q(titulo__icontains=termo_busca) | 
            Q(artista__nome__icontains=termo_busca)
        )
    
    obras = obras.order_by('ano_producao')
    
    contexto = {
        'obras': obras,
        'termo_busca': termo_busca,
    }
    
    return render(request, 'tessera/galeria.html', context=contexto)

# View para a página de detalhes de uma obra específica
def detalhe_obra(request, id_unico):
    obra = get_object_or_404(ObraDeArte, id_unico=id_unico)
    contexto = {
        'obra': obra
    }
    return render(request, 'tessera/detalhe_obra.html', context=contexto)
