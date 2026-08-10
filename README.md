# FastAPI Portfolio API

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688.svg)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-336791.svg)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED.svg)](https://www.docker.com/)

API RESTful production-ready para portfólio: **FastAPI**, **SQLAlchemy 2**, **Pydantic v2** e **PostgreSQL**, orquestrada com **Docker Compose**.

## Arquitetura

Camadas simples em `app/`:

| Arquivo | Responsabilidade |
|---------|------------------|
| `config.py` | Settings (`pydantic-settings`) |
| `database.py` | Engine, session, `get_db` |
| `models.py` | ORM (`Item`) |
| `schemas.py` | DTOs Pydantic |
| `crud.py` | Queries |
| `routers/items.py` | Endpoints REST |
| `main.py` | App + startup |

## Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- Git

## Fast-track

```bash
docker compose up --build
```

API em `http://localhost:8000`

## Documentação interativa

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Endpoints

| Método | Path | Status |
|--------|------|--------|
| POST | `/items/` | 201 |
| GET | `/items/` | 200 (`skip`, `limit`) |
| GET | `/items/{item_id}` | 200 / 404 |
| DELETE | `/items/{item_id}` | 204 / 404 |

## Variáveis de ambiente

Copie `.env.example` para `.env` se quiser sobrescrever defaults.

| Variável | Descrição | Default (exemplo) |
|----------|-----------|-------------------|
| `POSTGRES_USER` | Usuário Postgres | `postgres` |
| `POSTGRES_PASSWORD` | Senha Postgres | `postgres` |
| `POSTGRES_DB` | Nome do banco | `fastapi_db` |
| `DATABASE_URL` | URL SQLAlchemy | `postgresql://postgres:postgres@db:5432/fastapi_db` |

## Desenvolvimento local (sem Docker na API)

```bash
python -m venv venv
# Windows: venv\Scripts\activate
pip install -r requirements.txt
# Postgres local + DATABASE_URL apontando para localhost
uvicorn app.main:app --reload
```

## Parar e limpar volumes

```bash
docker compose down -v
```
