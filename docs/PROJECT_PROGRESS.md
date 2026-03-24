# Project Progress — NordOps Ticketing Service

## Overview

This document summarizes the progress and scope of the NordOps Ticketing Service project.

The project is designed as a hands-on DevOps portfolio demonstrating:

- Backend service development
- Containerization
- Kubernetes deployment
- Observability
- CI/CD automation

---

## EPIC 1 — API Foundation

### Goal

Build a minimal production-ready FastAPI service.

### Implemented

- `/healthz` endpoint (liveness)
- `/readyz` endpoint (readiness placeholder)
- OpenAPI documentation (`/docs`)
- Environment-based configuration
- Structured logging
- `.env.example`

---

## EPIC 2 — Ticketing API

### Goal

Implement core business logic.

### Implemented

- Ticket schema (id, title, description, status)
- Pydantic validation
- CRUD endpoints:
  - create ticket
  - list tickets
  - update ticket
  - delete ticket
- Initially implemented in-memory

---

## EPIC 3 — Database Integration

### Goal

Persist data using PostgreSQL.

### Implemented

- PostgreSQL via Docker Compose
- SQLAlchemy integration
- Alembic migrations
- `/readyz` checks DB connectivity
- CRUD operations moved from memory to DB

---

## EPIC 4 — Containerization

### Goal

Make the service portable.

### Implemented

- Dockerfile for FastAPI app
- Non-root container user
- `.dockerignore`
- Entrypoint script
- Multi-stage container best practices

---

## EPIC 5 — Kubernetes Deployment

### Goal

Run the system on Kubernetes.

### Implemented

- k3s cluster setup
- Namespace (`ticketing`)
- Deployment (FastAPI)
- Service (ClusterIP)
- Ingress (host-based routing)
- ConfigMap and Secret
- PostgreSQL StatefulSet
- PersistentVolumeClaim
- Liveness & Readiness probes

---

## EPIC 6 — Observability

### Goal

Add monitoring and visibility.

### Implemented

- `/metrics` endpoint in FastAPI
- Prometheus deployment (Helm)
- Prometheus scraping configuration
- Grafana deployment
- Prometheus datasource in Grafana
- Basic dashboards

---

## EPIC 7 — CI/CD

### Goal

Automate build and deployment.

### Implemented

- GitHub Actions pipeline
- Docker image build
- Push to Docker Hub
- SSH-based deployment to VM
- Kubernetes rollout automation

---

## EPIC 9 — Documentation

### Goal

Make the project production-grade and presentable.

### Implemented

- README (complete project overview)
- High-Level Design (HLD)
- Low-Level Design (LLD)
- Runbook (troubleshooting guide)
- Architecture diagrams (Mermaid)
- Project progress tracking (this document)

---

## Current Status

```text
API:            ✅ Completed
Database:       ✅ Completed
Docker:         ✅ Completed
Kubernetes:     ✅ Completed
Observability:  ✅ Completed
CI/CD:          ✅ Completed
Documentation:  ✅ Completed





## Key Achievements

- Built a full-stack backend system from scratch

- Deployed on Kubernetes with persistent storage

- Implemented monitoring with Prometheus and Grafana

- Automated CI/CD pipeline

- Structured documentation for real-world usage



## Next Steps

Planned future improvements:

- Deploy to cloud (AWS / EKS)

- Add Terraform infrastructure provisioning

- Implement alerting (Prometheus Alertmanager)

- Improve Grafana dashboards

- Add authentication (JWT)

- Implement versioned Docker image tagging

---

## Notes

This project is intended to simulate a real-world DevOps workflow and demonstrate practical engineering skills across the full lifecycle of an application.
