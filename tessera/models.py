
# tessera/models.py
from django.db import models
import uuid

# --- Modelos para as "Choices" (Opções de Escolha) ---

class StatusChoices(models.TextChoices):
    DISPONIVEL = 'DIS', 'Disponível'
    VENDIDA = 'VEN', 'Vendida'
    EMPRESTIMO = 'EMP', 'Empréstimo'
    RESTAURACAO = 'RES', 'Em Restauração'
    ACERVO = 'ACE', 'Acervo Permanente'

class ModoAquisicaoChoices(models.TextChoices):
    COMPRA = 'COM', 'Compra'
    DOACAO = 'DOA', 'Doação'
    COMISSAO = 'CMS', 'Comissão'
    LEGADO = 'LEG', 'Legado'

class EstadoConservacaoChoices(models.TextChoices):
    EXCELENTE = 'EXC', 'Excelente'
    BOM = 'BOM', 'Bom'
    REGULAR = 'REG', 'Regular'
    RUIM = 'RUI', 'Ruim'
    FRAGMENTO = 'FRA', 'Fragmento'

class TipoObraDigitalChoices(models.TextChoices):
    IMAGEM = 'IMG', 'Imagem Estática'
    ANIMACAO = 'GIF', 'Animação/GIF'
    VIDEO = 'VID', 'Vídeo'
    INTERATIVA = 'INT', 'Arte Interativa'
    AR = 'AR', 'Realidade Aumentada (AR)'
    INSTALACAO = 'INSTALL', 'Instalação Digital'


# --- Modelo Principal: ObraDeArte ---

class ObraDeArte(models.Model):
    # 01 - IDENTIFICAÇÃO ESSENCIAL
    id_unico = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID Único")
    numero_registro = models.CharField(max_length=100, blank=True, null=True, verbose_name="Número de Registro/Tombo")
    titulo = models.CharField(max_length=255, verbose_name="Título")
    subtitulo = models.CharField(max_length=255, blank=True, null=True, verbose_name="Subtítulo")
    ano_producao = models.IntegerField(verbose_name="Ano de Produção")
    data_producao_texto = models.CharField(max_length=100, blank=True, null=True, verbose_name="Data de Produção (texto)")

    # 02 - CARACTERÍSTICAS FÍSICAS E TÉCNICAS
    tecnica_principal = models.CharField(max_length=255, blank=True, null=True, verbose_name="Técnica Principal")
    outras_tecnicas = models.TextField(blank=True, null=True, verbose_name="Outras Técnicas")
    materiais_suporte = models.CharField(max_length=255, blank=True, null=True, verbose_name="Materiais/Suporte")
    materiais_utilizados = models.TextField(blank=True, null=True, verbose_name="Materiais Utilizados")
    dimensoes_altura_cm = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Altura (cm)")
    dimensoes_largura_cm = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Largura (cm)")
    dimensoes_profundidade_cm = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Profundidade (cm)")
    dimensoes_texto = models.CharField(max_length=255, blank=True, null=True, verbose_name="Dimensões (texto)")
    peso_kg = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True, verbose_name="Peso (kg)")
    assinatura = models.CharField(max_length=255, blank=True, null=True, verbose_name="Assinatura")
    inscricoes_marcas = models.TextField(blank=True, null=True, verbose_name="Inscrições/Marcas")

    # 03 - CONTEXTO E CONTEÚDO
    descricao_conceitual = models.TextField(blank=True, null=True, verbose_name="Descrição Conceitual")
    descricao_iconografica = models.TextField(blank=True, null=True, verbose_name="Descrição Iconográfica")
    palavras_chave = models.CharField(max_length=500, blank=True, null=True, verbose_name="Palavras-chave")
    periodo_movimento = models.CharField(max_length=255, blank=True, null=True, verbose_name="Período/Movimento")
    geolocalizacao_producao = models.CharField(max_length=255, blank=True, null=True, verbose_name="Geolocalização da Produção")

    # 04 - HISTÓRICO E PROVENIÊNCIA
    historico_exposicoes = models.TextField(blank=True, null=True, verbose_name="Histórico de Exposições")
    proveniencia = models.TextField(blank=True, null=True, verbose_name="Proveniência")
    bibliografia_publicacoes = models.TextField(blank=True, null=True, verbose_name="Bibliografia/Publicações")

    # 05 - GESTÃO E ADMINISTRAÇÃO
    status = models.CharField(max_length=3, choices=StatusChoices.choices, default=StatusChoices.DISPONIVEL)
    localizacao_atual = models.CharField(max_length=255, blank=True, null=True, verbose_name="Localização Atual")
    proprietario_atual = models.CharField(max_length=255, blank=True, null=True, verbose_name="Proprietário Atual")
    data_aquisicao = models.DateField(blank=True, null=True, verbose_name="Data de Aquisição")
    modo_aquisicao = models.CharField(max_length=3, choices=ModoAquisicaoChoices.choices, blank=True, null=True, verbose_name="Modo de Aquisição")
    valor_seguro = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name="Valor do Seguro")
    data_ultima_avaliacao = models.DateField(blank=True, null=True, verbose_name="Data da Última Avaliação")
    
    # 06 - CONSERVAÇÃO
    estado_conservacao = models.CharField(max_length=3, choices=EstadoConservacaoChoices.choices, blank=True, null=True, verbose_name="Estado de Conservação")
    relatorio_condicao = models.TextField(blank=True, null=True, verbose_name="Relatório de Condição")
    historico_restauracao = models.TextField(blank=True, null=True, verbose_name="Histórico de Restauração")
    data_ultima_higienizacao = models.DateField(blank=True, null=True, verbose_name="Data da Última Higienização")
    recomendacoes_manuseio = models.TextField(blank=True, null=True, verbose_name="Recomendações de Manuseio")
    
    # 07 - MÍDIA E DOCUMENTAÇÃO DIGITAL
    url_imagem_alta = models.URLField(max_length=1024, blank=True, null=True, verbose_name="URL da Imagem de Alta Resolução")
    url_galeria_imagens = models.URLField(max_length=1024, blank=True, null=True, verbose_name="URL da Galeria de Imagens")
    copyright_imagem = models.CharField(max_length=255, blank=True, null=True, verbose_name="Copyright da Imagem")

    # 08 - ARTE DIGITAL
    tipo_obra_digital = models.CharField(max_length=7, choices=TipoObraDigitalChoices.choices, blank=True, null=True, verbose_name="Tipo de Obra Digital")
    formato_arquivo_original = models.CharField(max_length=50, blank=True, null=True, verbose_name="Formato do Arquivo Original")
    formato_arquivo_exibicao = models.CharField(max_length=50, blank=True, null=True, verbose_name="Formato do Arquivo de Exibição")
    resolucao_dimensoes_px = models.CharField(max_length=100, blank=True, null=True, verbose_name="Resolução/Dimensões (px)")
    tamanho_arquivo_mb = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Tamanho do Arquivo (MB)")
    duracao = models.DurationField(blank=True, null=True, verbose_name="Duração (HH:MM:SS)")
    software_utilizado = models.TextField(blank=True, null=True, verbose_name="Software Utilizado")
    hardware_utilizado = models.TextField(blank=True, null=True, verbose_name="Hardware Utilizado")
    tecnica_glitch_aplicada = models.TextField(blank=True, null=True, verbose_name="Técnica de Glitch Aplicada")
    codigo_fonte_algoritmo = models.TextField(blank=True, null=True, verbose_name="Código-Fonte/Algoritmo")
    url_exibicao_online = models.URLField(max_length=1024, blank=True, null=True, verbose_name="URL de Exibição Online")
    dependencias_execucao = models.TextField(blank=True, null=True, verbose_name="Dependências de Execução")
    instrucoes_exibicao = models.TextField(blank=True, null=True, verbose_name="Instruções de Exibição")
    token_nft = models.CharField(max_length=255, blank=True, null=True, verbose_name="Token NFT")

    def __str__(self):
        return f"{self.titulo} ({self.ano_producao})"

    class Meta:
        ordering = ['-numero_registro', 'titulo']
        verbose_name = "Obra de Arte"
        verbose_name_plural = "Obras de Arte"