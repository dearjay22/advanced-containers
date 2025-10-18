# Advanced Containers Assignment

## Overview
This project sets up a containerized web application (Flask API) with a MySQL database. Docker Compose orchestrates containers, volumes, and networking. 

- Multi-stage Docker build for optimized image  
- Web app + MySQL container  
- Docker Compose orchestration  
- Volumes for persistence  
- Network isolation 

## Prerequisites
- Docker & Docker Compose installed
- Python 3.11 (for local dev if needed)

## Setup & Run

1. Copy `.env.example` to `.env` and modify credentials if needed:

```bash
cp .env.example .env
```

2. Build and start containers:

```bash
docker-compose up --build -d
```

3. Access API at: http://localhost:5000


## API Endpoints

- POST /user → Create a user

```bash
{"first_name":"John","last_name":"Doe"}
```

- GET /user/{id} → Get user by ID


## Security

- Non-root user in containers

- Minimal base image

- Environment variables for secrets

- Docker volumes for data persistence


## Testing

- Create a user:

```bash
curl -X POST http://localhost:5000/user -H "Content-Type: application/json" -d '{"first_name":"Alice","last_name":"Smith"}'
```

- Get user:

```bash
curl http://localhost:5000/user/1
```