# Decisões Técnicas

## 1. Contexto

Este documento registra as principais decisões técnicas da versão 0.1.0 do Sistema de Controle Financeiro API.

O objetivo desta versão é estabelecer uma base executável, com comunicação entre a API e o banco de dados, antes de implementar as regras de negócio financeiras.

## 2. Linguagem de programação

**Decisão:** Python 3.13.

**Justificativa:** Python oferece uma sintaxe acessível, um ecossistema amplo e bibliotecas adequadas para desenvolvimento de APIs e aplicações orientadas a dados.

A versão utilizada no ambiente local e no container da API é a série 3.13.

## 3. Framework da API

**Decisão:** FastAPI.

**Justificativa:** permite construir APIs HTTP com validação de dados, integração com tipagem Python e documentação interativa baseada em OpenAPI.

A documentação interativa é disponibilizada em `/docs`.

## 4. Servidor ASGI

**Decisão:** Uvicorn.

**Justificativa:** executa a aplicação FastAPI por meio da interface ASGI.

## 5. Banco de dados

**Decisão:** PostgreSQL 17.

**Justificativa:** oferece um banco de dados relacional adequado para armazenar futuramente receitas, despesas, categorias e registros financeiros históricos.

Nesta versão, o banco é inicializado e sua conectividade é validada. As entidades financeiras ainda não foram implementadas.

## 6. Acesso ao banco de dados

**Decisão:** SQLAlchemy 2.x com Psycopg 3.

**Justificativa:** SQLAlchemy fornece a camada de acesso ao banco de dados, enquanto Psycopg permite a comunicação entre Python e PostgreSQL.

A configuração atual utiliza uma conexão síncrona e valida a disponibilidade do banco por meio de uma consulta simples.

## 7. Configuração da aplicação

**Decisão:** Pydantic Settings e variáveis de ambiente.

**Justificativa:** permitem centralizar a configuração e separar os parâmetros de execução do código-fonte.

O arquivo `.env` é utilizado no ambiente local e não deve ser versionado. O arquivo `.env.example` serve como referência para a configuração.

## 8. Containerização e orquestração

**Decisão:** Docker e Docker Compose.

**Justificativa:** permitem executar a API e o banco de dados em ambientes isolados, reproduzíveis e coordenados.

O serviço da API depende da condição saudável do serviço PostgreSQL para iniciar no ambiente Compose.

## 9. Organização do código

**Decisão:** separar responsabilidades em módulos e diretórios.

A estrutura reserva áreas para:

- `api`: endpoints HTTP.
- `core`: configurações centrais.
- `domain`: regras e conceitos do domínio financeiro.
- `schemas`: estruturas de entrada e saída da API.
- `services`: lógica de aplicação.
- `repositories`: acesso e persistência de dados.
- `infrastructure`: integrações e recursos técnicos.
- `utils`: utilitários compartilhados.

Nem todas essas áreas possuem implementações nesta versão.

## 10. Verificação de saúde

**Decisão:** disponibilizar dois endpoints.

- `/health`: verifica se a API responde.
- `/health/db`: verifica se a aplicação consegue executar uma consulta no banco.

A separação permite distinguir a disponibilidade da API da disponibilidade do banco de dados.

## 11. Segurança e configuração local

O arquivo `.env` e outros dados locais devem permanecer fora do controle de versão. O `.dockerignore` impede que arquivos como `.env` e `.venv` sejam incluídos no contexto de construção da imagem.

As credenciais atuais destinam-se apenas ao ambiente de desenvolvimento. Ambientes compartilhados ou de produção exigirão gerenciamento apropriado de segredos.

## 12. Escopo e evolução

A versão 0.1.0 valida a infraestrutura inicial, sem implementar regras financeiras.

As próximas etapas poderão contemplar:

- Modelagem de receitas, despesas e categorias.
- Persistência e migrações do banco de dados.
- Validação das regras de negócio.
- Testes automatizados.
- Relatórios de orçamento e histórico financeiro.
- Autenticação e autorização, conforme os requisitos definidos.