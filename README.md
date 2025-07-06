#  Docker Boilerplate: Django + Postgres + PgAdmin

A ready-to-use Docker boilerplate that sets up a local development environment with **Python**, **Django**, **PostgreSQL**, and **pgAdmin**.

Simply clone the project, configure your environment with the provided `.env.template`, and start developing in minutes!

## 🚀 Features

Docker
Docker desktop (optional but recommended)

## 🚀 Features


- Django app running on Python
- PostgreSQL database
- pgAdmin for visual DB management
- `.env` support for easy configuration
- Isolated and reproducible dev environment with Docker

## Installation

**Clone the repository**

	cd your-repo

Create the .env file

	cp .env.template .env


Build the Docker containers:

	docker compose build

Start the containers:

	docker-compose up

## Default ports

Django development app

	http://localhost:8000/

PgAdmin PostgreSQL GUI

	http://localhost:5555/

## Volumes

PostgreSQL data is persisted using Docker volumes to avoid data loss across container restarts.

## Stopping and cleaning up

To stop the running containers:

	docker compose down

To stop and remove volumes (use with caution):

	docker compose down -v

## Conclusions

Of course you can use tools like Docker desktop to easily manage your containers.
