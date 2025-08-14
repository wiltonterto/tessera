from django.contrib import admin
from .models import ObraDeArte, Artista

# Registre o modelo Artista
@admin.register(Artista)
class ArtistaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_nascimento')
    search_fields = ('nome',)

# Usamos o @admin.register como uma forma moderna de registrar o modelo com a classe de customização
@admin.register(ObraDeArte)
class ObraDeArteAdmin(admin.ModelAdmin):
    # Usando fieldsets para criar as seções que você planejou
    fieldsets = [
        ('01 - Identificação Essencial', {
            'fields': (
                'titulo', 'subtitulo', 'artista', 'ano_producao', 
                'data_producao_texto', 'timestamp_producao', 'numero_registro'
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
            'fields': ('imagem_principal', 'url_galeria_imagens', 'copyright_imagem')
        }),
        ('08 - Arte Digital (Glitch Art)', {
        'classes': ('collapse',),
        'description': 'Preencha apenas os campos relevantes para o tipo de obra digital.',
        'fields': (
            'tipo_obra_digital', 
            # A linha dos formatos agora tem os 3 novos campos
            ('formato_imagem_estatica', 'formato_animacao', 'formato_video'),
            'resolucao_dimensoes_px', 'tamanho_arquivo_mb', 'duracao',)
        }),
        ('09 - Registro de Alterações', {
            'classes': ('collapse',),
            'fields': ('justificativa_ultima_alteracao',)
        }),
    ]

    # Melhora a visualização da lista de obras
    list_display = ('titulo', 'ano_producao', 'numero_registro', 'status')
    list_filter = ('status', 'artista', 'ano_producao', 'tecnica_principal')
    search_fields = ('titulo', 'numero_registro')

    