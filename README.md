# Sistema de Controle Financeiro API

API REST para servir como base de um sistema de controle financeiro pessoal, desenvolvido em Python.

## Status do projeto

**Versão:** 0.1.0 — Walking Skeleton

Esta versão estabelece a estrutura inicial da aplicação e valida a comunicação entre a API e o banco de dados PostgreSQL.

## Tecnologias utilizadas

- Python 3.13
- FastAPI
- Uvicorn
- SQLAlchemy 2.x
- PostgreSQL 17
- Psycopg 3
- Pydantic Settings
- Docker
- Docker Compose

## Funcionalidades implementadas

- Endpoint de verificação de saúde da API: `GET /health`.
- Endpoint de verificação de conexão com o banco: `GET /health/db`.
- Documentação interativa da API com Swagger UI.
- Inicialização da API e do PostgreSQL com Docker Compose.
- Configuração de variáveis de ambiente.

## Pré-requisitos

- Docker Desktop com Docker Compose.
- Git.
- Python 3.13 para execução e desenvolvimento local fora dos containers.
- Arquivo `.env` configurado na raiz do projeto.

## Configuração e execução

### 1. Configurar as variáveis de ambiente

Crie o arquivo `.env` na raiz do projeto utilizando `.env.example` como referência.

Preencha as variáveis necessárias com os valores apropriados para seu ambiente local.

**Não versione o arquivo `.env` nem publique credenciais reais.**

### 2. Iniciar a aplicação

Na raiz do projeto, execute:

```powershell
docker compose up -d
```

Esse comando inicia a API e o PostgreSQL em containers.

### 3. Verificar os serviços

Consulte o estado dos containers:

```powershell
docker compose ps
```

Para consultar os logs:

```powershell
docker compose logs
```

### 4. Acessar a API

Com os serviços em execução:

- Verificação da API: http://127.0.0.1:8000/health
- Verificação do banco: http://127.0.0.1:8000/health/db
- Documentação interativa: http://127.0.0.1:8000/docs

### 5. Encerrar os serviços

```powershell
docker compose down
```

O volume persistente do PostgreSQL é mantido por esse comando. Para remover também os dados persistidos, seria necessário solicitar explicitamente a remoção do volume.

## Estrutura do projeto

```text
app/
├── api/
│   └── health.py
├── core/
│   └── config.py
├── domain/
├── infrastructure/
│   └── database.py
├── repositories/
├── schemas/
├── services/
├── utils/
└── main.py

docker/
└── Dockerfile

docs/
tests/
docker-compose.yml
requirements.txt
.env.example
.gitignore
.dockerignore
README.md
```

As pastas ainda vazias representam áreas reservadas para a evolução da aplicação.

## Escopo da versão 0.1.0

Esta versão concentra-se na infraestrutura inicial. O cadastro de receitas e despesas, o histórico financeiro, as categorias de gastos, as regras de orçamento, as migrações e a autenticação ainda não fazem parte do escopo implementado.

## Próximos passos

- Definir os requisitos funcionais e as regras financeiras.
- Modelar as entidades do domínio.
- Implementar persistência e migrações do banco.
- Desenvolver as operações de receitas e despesas.
- Criar testes automatizados.
- Implementar relatórios e comparações entre gastos previstos e realizados.