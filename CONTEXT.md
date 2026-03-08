# Note App — Django Backend Context

## Project Purpose

REST API for a note-taking app built as a job assessment.
The frontend is a Next.js app consuming this API.

## Stack

- Django 5 + Django REST Framework
- PostgreSQL (via psycopg2)
- SimpleJWT for authentication
- Docker + docker-compose for local dev

## Architecture Rules

- All endpoints live under /api/v1/
- Use ViewSets + Routers (not function-based views)
- Always use IsAuthenticated permission unless explicitly noted
- Notes are always scoped to request.user — never return another user's notes
- Use environment variables for all secrets (SECRET*KEY, DB*\*)
- Follow PEP8. Add docstrings to all views and serializers.
- Use full import path(core.models, users.views)
- Split import by category using comments in the following order: Base python first without comment, # Django(Ex: from django...), # Third Party, # Local

## Models

### User

- Uses Django's default AbstractUser
- Auth via email (USERNAME_FIELD = 'email')

### Note

Categories: Random Thoughts, School, Personal

- title: CharField(max_length=255)
- body: TextField(blank=True)
- color: CharField(max_length=7, default='#ffffff') # hex color
- category: CharField(max_length=255, options=Categories)
- owner: ForeignKey(User, on_delete=CASCADE)
- created_at: auto
- updated_at: auto

## API Endpoints

- POST /api/v1/auth/register/
- POST /api/v1/auth/login/ → returns access + refresh JWT
- POST /api/v1/auth/refresh/
- GET /api/v1/notes/ → list (filter: category)
- POST /api/v1/notes/
- GET /api/v1/notes/{id}/
- PATCH /api/v1/notes/{id}/

## Error Format

Always return errors as: { "error": "message" } with appropriate HTTP status codes.

## Testing

Use pytest + pytest-django. Cover: auth flow, CRUD ownership rules, summarize endpoint.
