from django.contrib import admin
from .models import ObraDeArte

# Usamos o @admin.register como uma forma moderna de registrar o modelo com a classe de customização
@admin.register(ObraDeArte)
class ObraDeArteAdmin(admin.ModelAdmin):
    # Usando fieldsets para criar as seções que você planejou
    fieldsets = [
        ('01 - Identificação Essencial', {
            'fields': (
                'titulo', 'subtitulo', 'ano_producao', 
                'data_producao_texto', 'numero_registro'
            )
        }),
        ('02 - Características Físicas e Técnicas', {
            'classes': ('collapse',), # Esta seção começa recolhida
            'fields': (
                'tecnica_principal', 'outras_tecnicas', 'materiais_suporte', 
                'materiais_utilizados', 'assinatura', 'inscricoes_marcas', 
                ('dimensoes_altura_cm', 'dimensoes_largura_cm', 'dimensoes_profundidade_cm'), 
                'dimensoes_texto', 'peso_kg'
            )
        }),
        ('03 - Contexto e Conteúdo', {
            'classes': ('collapse',),
            'fields': (
                'descricao_conceitual', 'descricao_iconografica', 
                'palavras_chave', 'periodo_movimento', 'geolocalizacao_producao'
            )
        }),
        ('04 - Histórico e Proveniência', {
            'classes': ('collapse',),
            'fields': ('historico_exposicoes', 'proveniencia', 'bibliografia_publicacoes')
        }),
        ('05 - Gestão e Administração', {
            'classes': ('collapse',),
            'fields': (
                'status', 'localizacao_atual', 'proprietario_atual', 
                'data_aquisicao', 'modo_aquisicao', 'valor_seguro', 
                'data_ultima_avaliacao'
            )
        }),
        ('06 - Conservação', {
            'classes': ('collapse',),
            'fields': (
                'estado_conservacao', 'relatorio_condicao', 'historico_restauracao',
                'data_ultima_higienizacao', 'recomendacoes_manuseio'
            )
        }),
        ('07 - Mídia e Documentação', {
            'classes': ('collapse',),
            'fields': ('url_imagem_alta', 'url_galeria_imagens', 'copyright_imagem')
        }),
        ('08 - Arte Digital (Glitch Art)', {
            'classes': ('collapse',),
            'description': 'Preencha apenas se for uma obra digital.', # Adiciona um texto de ajuda
            'fields': (
                'tipo_obra_digital', 'formato_arquivo_original', 'formato_arquivo_exibicao', 
                'resolucao_dimensoes_px', 'tamanho_arquivo_mb', 'duracao', 
                'software_utilizado', 'hardware_utilizado', 'tecnica_glitch_aplicada', 
                'codigo_fonte_algoritmo', 'url_exibicao_online', 'dependencias_execucao', 
                'instrucoes_exibicao', 'token_nft'
            )
        }),
    ]

    # Melhora a visualização da lista de obras
    list_display = ('titulo', 'ano_producao', 'numero_registro', 'status')
    list_filter = ('status', 'ano_producao', 'tecnica_principal')
    search_fields = ('titulo', 'numero_registro')