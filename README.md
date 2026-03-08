# Note App — Backend

REST API for a note-taking app built as a job assessment. Consumed by the Next.js frontend in `note-app-turbo`.

## Tech Stack

| | |
|---|---|
| Framework | Django 5 + Django REST Framework |
| Database | PostgreSQL 16 |
| Auth | SimpleJWT (access + refresh tokens) |
| API Docs | drf-spectacular (OpenAPI 3, Swagger UI, ReDoc) |
| Config | django-environ |
| Containerization | Docker + docker-compose |
| Testing | pytest + pytest-django |

## API Documentation

Interactive docs are available when the server is running:

| UI | URL |
|---|---|
| Swagger UI | `/api/schema/swagger/` |
| ReDoc | `/api/schema/redoc/` |
| OpenAPI schema (JSON/YAML) | `/api/schema/` |

## API Endpoints

All endpoints are prefixed with `/api/v1/`.

| Method | Endpoint | Auth | Description |
|---|---|---|---|
| GET | `/health/` | No | Service health check |
| POST | `/auth/register/` | No | Register a new user |
| POST | `/auth/login/` | No | Login, returns access + refresh JWT |
| POST | `/auth/refresh/` | No | Refresh access token |
| GET | `/notes/` | Yes | List notes (filter: `?category=`) |
| POST | `/notes/` | Yes | Create a note |
| GET | `/notes/{id}/` | Yes | Get a single note |
| PATCH | `/notes/{id}/` | Yes | Update a note |

Notes are always scoped to the authenticated user.

## Error Format

All errors are returned as:

```json
{ "error": { "field": ["message"] } }
```

## Project Structure

```
note-app-turbo-backend/
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── apps/
│   ├── users/        # Custom user model (email-based auth)
│   └── notes/        # Notes CRUD
├── manage.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── .env.example
```

## Getting Started

### Prerequisites

- Docker & docker-compose

### Setup

```bash
cp .env.example .env
# Edit .env if needed (defaults work out of the box with docker-compose)
```

### Run with Docker

```bash
docker-compose up --build
```

The API will be available at [http://localhost:8000](http://localhost:8000).

Migrations run automatically on startup via `entrypoint.sh`.

### Run without Docker

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Set up a local PostgreSQL database and configure .env accordingly
python manage.py migrate
python manage.py runserver
```

### Environment Variables

| Variable | Description | Default |
|---|---|---|
| `SECRET_KEY` | Django secret key | — |
| `DEBUG` | Debug mode | `True` |
| `ALLOWED_HOSTS` | Comma-separated allowed hosts | `localhost,127.0.0.1` |
| `CORS_ALLOWED_ORIGINS` | Allowed CORS origins | `http://localhost:3000` |
| `DB_NAME` | PostgreSQL database name | `noteapp` |
| `DB_USER` | PostgreSQL user | `noteapp` |
| `DB_PASSWORD` | PostgreSQL password | `noteapp` |
| `DB_HOST` | PostgreSQL host | `db` |
| `DB_PORT` | PostgreSQL port | `5432` |

### Tests

```bash
pytest
```

## Models

### User

- Extends `AbstractUser`
- `USERNAME_FIELD = 'email'`

### Note

| Field | Type | Notes |
|---|---|---|
| `title` | CharField(255) | |
| `body` | TextField | blank allowed |
| `category` | CharField | `Random Thoughts`, `School`, `Personal` |
| `owner` | ForeignKey(User) | CASCADE |
| `created_at` | DateTimeField | auto |
| `updated_at` | DateTimeField | auto |

## Use of AI

Claude Code (Anthropic) was used throughout this project to assist with:

- Restructuring Django apps into an `apps/` directory (updating `name`, `INSTALLED_APPS`, and URL includes accordingly)
- Generating boilerplate file structure from the `CONTEXT.md` spec

All business logic, model design, API design, and final review were done by the developer.
