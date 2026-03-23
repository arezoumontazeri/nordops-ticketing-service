# NordOps Ticketing Service

A production-like ticketing service built to demonstrate modern DevOps and Cloud-Native engineering practices.

This project started as a simple FastAPI backend and evolved into a full platform-style application with:

- PostgreSQL persistence
- Docker containerization
- Kubernetes deployment
- Prometheus metrics
- Grafana dashboards
- CI/CD with GitHub Actions

The goal of this project is to simulate how a real backend service is built, deployed, monitored, and maintained in a production-oriented environment.

---

## Project Overview

NordOps Ticketing Service is a REST API for managing support-style tickets.

It supports:

- Creating tickets
- Listing tickets
- Updating tickets
- Deleting tickets
- Monitoring service health
- Exposing metrics for observability

This project is designed as a DevOps portfolio project and focuses on real deployment and operations workflows, not only backend development.

---

## Architecture

High-level request flow:

Client → Ingress → Kubernetes Service → FastAPI Application → PostgreSQL

Observability flow:

FastAPI `/metrics` → Prometheus → Grafana

CI/CD flow:

GitHub Push → GitHub Actions → Docker Build → Docker Hub → Kubernetes Deploy

---

## Tech Stack

### Backend

- Python
- FastAPI
- SQLAlchemy
- Alembic
- PostgreSQL

### Containerization

- Docker
- Docker Compose

### Kubernetes

- k3s
- Deployment
- Service
- Ingress
- ConfigMap
- Secret
- StatefulSet
- PersistentVolumeClaim

### Observability

- Prometheus
- Grafana

### CI/CD

- GitHub Actions
- Docker Hub

---

## Features

- REST API for ticket management
- PostgreSQL-backed persistent storage
- Database migrations with Alembic
- Dockerized application runtime
- Kubernetes deployment with ingress
- Liveness and readiness probes
- ConfigMap and Secret-based configuration
- Stateful PostgreSQL deployment
- Prometheus metrics endpoint
- Grafana integration
- Automated build and deployment pipeline

---

## Repository Structure

```text
nordops-ticketing-service/
├── app/
│   ├── api/
│   ├── core/
│   ├── db/
│   └── main.py
├── alembic/
├── docker/
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── entrypoint.sh
├── k8s/
│   └── base/
├── monitoring/
├── .github/
│   └── workflows/
├── requirements.txt
└── README.md


```

## Local Development

---
---  
  ### Run the API locally  

```bash  
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

### Health checks

curl http://localhost:8000/healthz  
curl http://localhost:8000/readyz

---

## Run with Docker

### Build image

docker build -f docker/Dockerfile -t nordops-ticketing:dev .

### Run with Docker Compose

docker compose -f docker/docker-compose.yml up --build

---

## Run on Kubernetes

This project is deployed locally on k3s.

Main Kubernetes resources:

- Namespace
- Deployment
- Service
- Ingress
- ConfigMap
- Secret
- PostgreSQL StatefulSet
- PersistentVolumeClaim

### Example commands

kubectl get pods -n ticketing  
kubectl get svc -n ticketing  
kubectl get ingress -n ticketing

---

## Observability

The application exposes Prometheus-compatible metrics at:

/metrics

Prometheus scrapes the application metrics and Grafana is used for visualization.

Example metrics:

- `http_requests_total`
- `http_request_duration_seconds`

---

## CI/CD

GitHub Actions is used for CI/CD.

Current pipeline includes:

- Docker image build
- Push to Docker Hub
- Kubernetes deployment update

Flow:

1. Push to `main`
2. GitHub Actions builds image
3. Image is pushed to Docker Hub
4. Kubernetes deployment is updated

---
