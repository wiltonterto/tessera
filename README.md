# Tessera - Sistema de Gerenciamento de Acervo para Artistas

Uma ferramenta de catalogação robusta, projetada para o dia a dia de artistas visuais, de todos os suportes — do tradicional ao digital.

## O Problema

Artistas, especialmente os independentes e mais tradicionais, muitas vezes gerenciam seus acervos de forma descentralizada e manual, usando planilhas, documentos de texto e pastas de imagens. Esse processo é propenso a erros, dificulta a consulta e a geração de documentos importantes, e consome um tempo precioso que poderia ser usado para criar.

A proposta do **Tessera** é centralizar todas as informações do acervo em um único lugar, de forma intuitiva, segura e inteligente, facilitando não apenas o registro, mas também a gestão da carreira do artista.

## Funcionalidades Atuais (Versão de Desenvolvimento)

* **Catalogação Detalhada:** Um modelo de dados completo com mais de 50 campos, cobrindo desde a identificação essencial e características físicas até o histórico de exposições, dados de conservação e metadados de arte digital.
* **Interface Administrativa Organizada:** Formulários de cadastro divididos em seções lógicas e recolhíveis para um preenchimento limpo e focado.
* **Busca e Filtros Avançados:** Ferramentas de busca por texto e filtros por ano, técnica e status, permitindo uma consulta rápida e eficiente do acervo.
* **Suporte Híbrido:** Estrutura flexível que acomoda tanto obras físicas (pinturas, esculturas) quanto digitais (imagens, vídeos, glitch art).

## Roadmap de Futuras Funcionalidades

O objetivo é transformar o Tessera em um verdadeiro assistente para o artista. Os próximos passos planejados incluem:

-   [ ] **Upload Direto de Mídia:** Permitir o upload dos arquivos de imagem/vídeo diretamente pelo formulário.
-   [ ] **Notificações Inteligentes:** Criação de um sistema de alertas automáticos para datas importantes, como a próxima higienização de uma obra.
-   [ ] **Assistente de Documentação (IA):** O grande diferencial. Utilizar IA para gerar, a partir dos dados catalogados, documentos essenciais como:
    -   Memoriais descritivos
    -   Propostas de venda
    -   Termos de empréstimo para exposições
-   [ ] **Galeria Pública (Opcional):** Possibilidade de criar uma galeria online pública, selecionando quais obras do acervo serão exibidas.

## Tecnologias

* **Backend:** Python com o framework Django.
* **Banco de Dados:** SQLite3 (para desenvolvimento).

## Como Rodar Localmente

1.  Clone este repositório.
2.  Crie e ative um ambiente virtual: `python -m venv venv` e `.\venv\Scripts\activate`.
3.  Instale as dependências: `pip install django`.
4.  Execute as migrações do banco de dados: `python manage.py migrate`.
5.  Crie um superusuário: `python manage.py createsuperuser`.
6.  Inicie o servidor de desenvolvimento: `python manage.py runserver`.

---
_Este é um projeto de aprendizado e está em constante desenvolvimento. Criado por Wilton Terto._