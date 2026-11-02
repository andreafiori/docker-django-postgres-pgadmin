# Docker Boilerplate: Django + Postgres + pgAdmin

A ready-to-use Docker boilerplate that sets up a local development environment with **Python 3.13**, **Django 5.2 (LTS)**, **PostgreSQL 16**, and **pgAdmin**.

Simply clone the project, configure your environment with the provided `.env.template`, and start developing in minutes!

## Requirements

- Docker (Docker Desktop optional but recommended)
- Docker Compose v2 (bundled with Docker Desktop)

## Features

- Django app served by Gunicorn (non-root user, healthcheck)
- PostgreSQL 16 with healthcheck + boot ordering via `depends_on`
- pgAdmin with persistent storage for visual DB management
- `.env` support for easy configuration
- Debug overlay (`docker-compose.debug.yml`) with `debugpy` for remote debugging

## Installation

**Clone the repository**

```sh
cd your-repo
```

**Create the `.env` file**

```sh
cp .env.template .env
```

**Build the Docker containers**

```sh
docker compose build
```

**Start the containers**

```sh
docker compose up -d
```

## Default ports

| Service | URL |
|---|---|
| Django dev app | http://localhost:8000/ |
| PostgreSQL (localhost only) | localhost:6543 |
| pgAdmin | http://localhost:5555/ |

All ports can be overridden in `.env` (`DJANGO_PORT`, `POSTGRES_PORT`, `PGADMIN_PORT`).

## Debugging

Start with the debug overlay (waits for a VS Code / remote debugger client on port `5678`):

```sh
docker compose -f docker-compose.yml -f docker-compose.debug.yml up
```

## Volumes

PostgreSQL data and pgAdmin user data are persisted using named Docker volumes to avoid data loss across container restarts.

## Stopping and cleaning up

To stop the running containers:

```sh
docker compose down
```

To stop and remove volumes (use with caution):

```sh
docker compose down -v
```
