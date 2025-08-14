# Tessera - Sistema de Gerenciamento de Acervo para Artistas

Uma ferramenta de catalogação robusta, projetada para o dia a dia de artistas visuais, abrangendo todos os suportes — do tradicional ao digital.

## O Problema

Artistas, especialmente independentes e tradicionais, muitas vezes gerenciam seus acervos de forma descentralizada e manual, usando planilhas, documentos de texto e pastas de imagens. Esse processo é propenso a erros, dificulta a consulta, atrapalha a geração de documentos importantes e consome tempo que poderia ser usado para criar.

O **Tessera** centraliza todas as informações do acervo em um único lugar, de forma intuitiva, segura e inteligente, facilitando não apenas o registro, mas também a gestão da carreira artística.

## Funcionalidades Atuais (Versão de Desenvolvimento)

- **Modelo de Dados Completo:** Estrutura com mais de 50 campos, cobrindo informações físicas, digitais, de conservação, administrativas e de proveniência.
- **Relacionamento de Artistas:** Sistema de cadastro de artistas interligado com as obras.
- **Admin Customizado e Profissional:** Interface de gerenciamento com seções organizadas, filtros avançados por status, ano e artista, e busca textual.
- **Suporte a Upload de Imagens:** Envio de imagens diretamente pelo formulário.
- **Visualização em Galeria:** Página dedicada para visualização das obras em formato de galeria, filtrando por artista ou palavra-chave.
- **Dashboard Resumido:** Visão geral do acervo, com indicadores rápidos e estatísticas.

## Roadmap de Futuras Funcionalidades

O objetivo é transformar o Tessera em um verdadeiro assistente para o artista. Os próximos passos planejados incluem:

- [ ] **Upload Direto de Mídia:** Permitir o envio de imagens e vídeos diretamente pelo formulário.
- [ ] **Notificações Inteligentes:** Alertas automáticos para datas importantes, como a próxima higienização de uma obra.
- [ ] **Assistente de Documentação (IA):** Geração automática de documentos essenciais a partir dos dados catalogados, como:
    - Memoriais descritivos
    - Propostas de venda
    - Termos de empréstimo para exposições
- [ ] **Galeria Pública (Opcional):** Possibilidade de criar uma galeria online pública, selecionando quais obras serão exibidas.

## Tecnologias Utilizadas

- **Backend:** Python (Django)
- **Banco de Dados:** SQLite3 (desenvolvimento)
- **Frontend:** HTML, CSS e templates Django

## Como Rodar Localmente

1. Clone este repositório:
   ```bash
   git clone https://github.com/wiltonterto/tessera.git

