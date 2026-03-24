# High-Level Design (HLD)

## 1. Overview

NordOps Ticketing Service is a cloud-native backend application designed to demonstrate modern DevOps practices including containerization, orchestration, observability, and CI/CD.

The system exposes a REST API for managing tickets and is deployed on Kubernetes with full monitoring and automated deployment.

---

## 2. System Components

The system consists of the following main components:

### 1. Client

- Sends HTTP requests to the system
- Can be curl, browser, or any API client

### 2. Ingress (Kubernetes)

- Entry point to the cluster
- Routes external traffic to internal services
- Host-based routing (`ticketing.local`)

### 3. Service (ClusterIP)

- Internal load balancer
- Routes traffic to application pods

### 4. Application (FastAPI)

- Core business logic
- Exposes REST endpoints:
  - `/tickets`
  - `/healthz`
  - `/readyz`
  - `/metrics`

### 5. Database (PostgreSQL)

- Stores ticket data
- Runs as a StatefulSet
- Uses persistent storage (PVC)

### 6. Config & Secrets

- ConfigMap: non-sensitive configs
- Secret: database credentials

### 7. Observability Stack

- Prometheus: collects metrics
- Grafana: visualizes metrics

### 8. CI/CD Pipeline

- GitHub Actions
- Builds Docker image
- Pushes to Docker Hub
- Deploys to Kubernetes via SSH

---

## 3. Request Flow

```text
Client
  ↓
Ingress
  ↓
Service
  ↓
FastAPI Pod
  ↓
PostgreSQL

#### Steps

1. Client sends request (e.g., create ticket)

2. Ingress routes request to service

3. Service forwards to one of the pods

4. FastAPI processes request

5. Data is stored/retrieved from PostgreSQL

6. Response returned to client



---

## Observability Flow

FastAPI (/metrics)
  ↓
Prometheus
  ↓
Grafana

#### Steps:

1. Application exposes metrics at `/metrics`

2. Prometheus scrapes metrics periodically

3. Grafana queries Prometheus

4. Dashboards display system behavior

---

## 5. CI/CD Flow

GitHub Push
  ↓
GitHub Actions
  ↓
Docker Build
  ↓
Docker Hub
  ↓
SSH to VM
  ↓
kubectl rollout restart

#### Steps:

1. Code pushed to main branch

2. GitHub Actions pipeline starts

3. Docker image is built

4. Image is pushed to Docker Hub

5. Pipeline connects to VM via SSH

6. Kubernetes deployment is updated

7. New pods are rolled out

---

## 6. Deployment Architecture

- Kubernetes (k3s)

- Single-node cluster (local VM)

- Namespaced isolation (`ticketing`)

- Stateless app + stateful DB

---

## 7. Key Design Decisions

### Containerization

- Ensures consistent runtime across environments

### Kubernetes Deployment

- Enables scalability and self-healing

### Stateful Database

- PostgreSQL uses StatefulSet + PVC for persistence

### Separation of Concerns

- App, DB, monitoring are separate components

### Observability First

- Metrics exposed and monitored from early stages

### CI/CD Automation

- Eliminates manual deployment steps

---

## 8. Scalability Considerations

- App can scale horizontally (multiple pods)

- Service load balances traffic

- DB is currently single instance (can be improved later)

---

## 9. Future Improvements

- Multi-node Kubernetes cluster

- Horizontal Pod Autoscaling (HPA)

- Managed database (RDS)

- Alerting (Prometheus Alertmanager)

- Canary deployments
