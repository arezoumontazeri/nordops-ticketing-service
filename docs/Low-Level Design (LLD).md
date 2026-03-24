# Low-Level Design (LLD)

## 1. Overview

This document describes the internal design of the NordOps Ticketing Service.

It focuses on:

- API structure
- request/response models
- database model
- configuration handling
- logging
- metrics
- deployment behavior

---

## 2. Application Structure

Main code structure:
app/
├── api/
│   ├── routes/
│   │   ├── health.py
│   │   ├── tickets.py
│   │   └── metrics.py
│   └── schemas.py
├── core/
│   ├── config.py
│   └── logging.py
├── db/
│   ├── models.py
│   └── session.py
└── main.py

### Responsibilities

- `main.py`
  
  - creates FastAPI app
  
  - registers routers
  
  - registers middleware

- `api/routes/*`
  
  - HTTP endpoints

- `api/schemas.py`
  
  - request and response validation

- `core/config.py`
  
  - environment-based settings

- `core/logging.py`
  
  - application logging setup

- `db/models.py`
  
  - SQLAlchemy models

- `db/session.py`
  
  - database engine and session management

---

## 3. API Endpoints

### Health Endpoints

#### `GET /healthz`

Purpose:

- checks whether the application process is alive

Response:

{"status": "ok"}

#### `GET /readyz`

Purpose:

- checks whether the application is ready to serve traffic

- validates database connectivity

Success response:

{"status": "ready"}

Failure response:

{"detail": "Database not ready"}

---

### Ticket Endpoints

#### `POST /tickets`

Creates a new ticket.

Request:

{  
  "title": "Cannot login",  
  "description": "Login page returns error"  
}

Response:

{  
  "id": "uuid",  
  "title": "Cannot login",  
  "description": "Login page returns error",  
  "status": "open"  
}

---

#### `GET /tickets`

Returns all tickets.

---

#### `GET /tickets/{id}`

Returns a single ticket by ID.

---

#### `PATCH /tickets/{id}`

Updates ticket fields such as:

- title

- description

- status

---

#### `DELETE /tickets/{id}`

Deletes a ticket.

---

### Metrics Endpoint

#### `GET /metrics`

Purpose:

- exposes Prometheus-compatible metrics

Example metrics:

- `http_requests_total`

- `http_request_duration_seconds`

---

## 4. Schemas

Defined in:

app/api/schemas.py

### TicketCreate

Fields:

- `title: str`

- `description: Optional[str]`

Validation:

- title must have minimum length

- title must have maximum length

### TicketUpdate

Fields:

- `title: Optional[str]`

- `description: Optional[str]`

- `status: Optional[str]`

### TicketOut

Fields:

- `id: str`

- `title: str`

- `description: Optional[str]`

- `status: str`

---

## 5. Database Design

Database: PostgreSQL

ORM: SQLAlchemy

Migration tool: Alembic

### Main Table: `tickets`

Columns:

- `id`

- `title`

- `description`

- `status`

Logical ticket fields:

- `id`: unique identifier

- `title`: short ticket summary

- `description`: optional detailed text

- `status`: ticket state (`open`, `in_progress`, `resolved`, `closed`)

---

## 6. Database Access Layer

Defined in:

app/db/session.py

Responsibilities:

- create SQLAlchemy engine

- create DB sessions

- provide `get_db()` dependency for FastAPI routes

Flow:

Request
  ↓
FastAPI dependency injection
  ↓
DB session created
  ↓
Route handler uses session
  ↓
Session closed after request

---

## 7. Configuration Handling

Defined in:

app/core/config.py

Configuration is loaded from environment variables.

Examples:

- `APP_NAME`

- `LOG_LEVEL`

- `DATABASE_URL`

This allows:

- local development

- Docker-based runtime

- Kubernetes ConfigMap/Secret integration

---

## 8. Logging

Defined in:

app/core/logging.py

Logging is structured and configurable by environment.

Purpose:

- startup visibility

- debugging

- operational traceability

---

## 9. Metrics Collection

Defined in:

app/api/routes/metrics.py

and middleware in:

app/main.py

Metrics collected:

- request count

- request latency

Instrumentation flow:


HTTP Request
  ↓
Middleware
  ↓
Counter increment
Histogram observe
  ↓
Prometheus scrape

---

## 10. Kubernetes Runtime Behavior

### Deployment

- runs the FastAPI application

- uses probes

- uses resource requests and limits

### Probes

- liveness: `/healthz`

- readiness: `/readyz`

### Service

- exposes app internally via ClusterIP

### Ingress

- exposes app externally via host routing

### ConfigMap

- non-sensitive runtime config

### Secret

- sensitive values / credentials

### PostgreSQL StatefulSet

- stable DB identity

- persistent volume-backed storage

---

## 11. Startup Behavior

Container startup flow:

Container starts
  ↓
Entrypoint script runs
  ↓
Alembic migrations executed
  ↓
FastAPI server starts

This ensures database schema is applied before serving traffic.

---

## 12. Error Handling

### Readiness Failure

If DB is unavailable:

- `/readyz` returns 503

### Ticket Lookup Failure

If ticket does not exist:

- ticket endpoints return 404

### Validation Failure

If request body is invalid:

- FastAPI returns 422

---

## 13. Security Considerations

Current implementation includes:

- separation of config and secrets in Kubernetes

- non-root container runtime

- restricted service exposure through Kubernetes resources

Potential future improvements:

- JWT authentication

- RBAC tightening

- secret externalization

- network policies

---

## 14. Future Low-Level Improvements

- add timestamps to DB model

- add test coverage

- add repository/service layer abstraction

- add alerting metrics

- add versioned image tagging
