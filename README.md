# NordOps Ticketing Service

A production-ready Ticketing Service built with FastAPI to demonstrate modern DevOps and Cloud Engineering best practices.

This project is part of my DevOps portfolio and focuses on building, containerizing, deploying, monitoring, and scaling a backend service using real-world production patterns.

---

## 🚀 Project Vision

This repository will evolve into a fully production-like backend system that includes:

- Clean backend architecture
- Docker containerization
- Kubernetes deployment with Helm
- Observability stack (Prometheus, Grafana, Loki)
- CI/CD automation with GitHub Actions
- Infrastructure as Code with Terraform
- AWS EKS deployment

The goal is to simulate a real-world production environment.

---

## 🏗 Planned Architecture

Client → Ingress → FastAPI API → PostgreSQL  
                           ↓  
                 Prometheus / Grafana / Loki  

A full architecture diagram will be added as the project evolves.

---

## 🧱 Tech Stack

### Backend

- Python 3.12
- FastAPI
- SQLAlchemy
- PostgreSQL

### DevOps & Infrastructure

- Docker
- Kubernetes
- Helm
- GitHub Actions
- Terraform

### Observability

- Prometheus
- Grafana
- Loki

### Cloud

- AWS (EKS, VPC, IAM)

---

## 📂 Project Structure (Initial Phase)

nordops-ticketing-service/
├─ app/
│ ├─ main.py
│ ├─ api/
│ ├─ core/
│ └─ tests/
├─ docker/
├─ k8s/
├─ observability/
├─ scripts/
└─ README.md

---

## 🔧 Current Status

- [ ] Repository initialized
- [ ] Basic FastAPI service
- [ ] Database integration
- [ ] Docker setup
- [ ] Kubernetes deployment
- [ ] Monitoring stack
- [ ] CI/CD pipeline
- [ ] AWS deployment

---

## 🩺 Health Endpoint

GET /healthz

Response:
{"status":"ok"}

---

## 📈 Development Roadmap

The service will progressively include:

- Structured JSON logging
- Readiness & liveness probes
- Metrics endpoint (/metrics)
- Horizontal Pod Autoscaling
- Infrastructure as Code
- Cloud-native deployment

---

## 🎯 Purpose of This Project

This project demonstrates:

- Production-oriented backend design
- DevOps automation practices
- Cloud-native architecture thinking
- Monitoring and observability setup
- Infrastructure as Code implementation

It reflects real-world backend and DevOps engineering workflows.

---

## 👩‍💻 Author

Arezou — DevOps-focused Engineer based in Gothenburg, Sweden.

---

## 📜 License

MIT
