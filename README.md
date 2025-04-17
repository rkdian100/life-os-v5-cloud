# Life OS v5 – Cloud Edition

## Features
- FastAPI backend
- JSON-based task, emotion, and reflection management
- Modular routes
- Dockerized

## Endpoints
- GET/POST `/tasks`
- GET/POST `/emotions`
- GET/POST `/reflections`
- GET `/health`

## Run
```bash
docker build -t lifeosv5 .
docker run -p 8000:8000 lifeosv5
```
