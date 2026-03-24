# Runbook / Troubleshooting Guide

## 1. Overview

This runbook documents common operational checks and troubleshooting steps for the NordOps Ticketing Service.

It covers:

- application health
- Kubernetes debugging
- database troubleshooting
- ingress troubleshooting
- Prometheus troubleshooting
- deployment issues

---

## 2. Basic Health Checks

### Check application health

```bash
curl -H "Host: ticketing.local" http://192.168.122.251/healthz
```

Expected response:

```json
{"status": "ok"}
```

---

### Check application readiness

```bash
curl -H "Host: ticketing.local" http://192.168.122.251/readyz
```

Expected response:

```json
{"status": "ready"}
```

If response is 503, database connectivity should be checked.

---

### Check metrics endpoint

```bash
curl -H "Host: ticketing.local" http://192.168.122.251/metrics
```

Expected result:

- Prometheus-compatible metrics output

---

## 3. Kubernetes Checks

### List pods

```bash
kubectl get pods -n ticketing
```

Healthy state:

- `ticketing-app` → `1/1 Running`

- `postgres-0` → `1/1 Running`

---

### Describe a pod

```bash
kubectl describe pod <pod-name> -n ticketing
```

Use this when:

- pod is not starting

- pod is not ready

- pod restarts repeatedly

Important section:

- `Events`

---

### Check pod logs

```bash
kubectl logs <pod-name> -n ticketing
```

Use this to inspect:

- application startup errors

- database connection issues

- migration failures

---

### Check environment variables inside pod

```bash
kubectl exec -it <pod-name> -n ticketing -- printenv
```

Useful for verifying:

- `DATABASE_URL`

- `APP_NAME`

- `LOG_LEVEL`

---

## 4. Common Application Issues

### Problem: `/healthz` works but `/readyz` returns 503

Possible cause:

- database is not reachable

Checks:

```bash
kubectl get pods -n ticketing
kubectl get svc -n ticketing
kubectl logs deployment/ticketing-app -n ticketing
```

Verify:

- postgres pod is running

- postgres service exists

- application has correct `DATABASE_URL`

---

### Problem: `/tickets` returns 500

Possible causes:

- DB connection issue

- migration not applied

- invalid configuration

Checks:

```bash
kubectl logs deployment/ticketing-app -n ticketing
kubectl exec -it postgres-0 -n ticketing -- psql -U postgres -d ticketing
```

Verify:

- DB is reachable

- required tables exist

---

## 5. Database Troubleshooting

### Check PostgreSQL pod

```bash
kubectl get pods -n ticketing
```

Expected:

- `postgres-0` should be `Running`

---

### Check PostgreSQL service

```bash
kubectl get svc -n ticketing
```

Expected:

- service named `postgres`

---

### Connect to PostgreSQL directly

```bash
kubectl exec -it postgres-0 -n ticketing -- psql -U postgres -d ticketing
```

Useful queries:

```sql
SELECT 1;
\dt
```

Use this to verify:

- database is accessible

- tables exist

---

### Check persistent volume claim

```bash
kubectl get pvc -n ticketing
```

Expected:

- PVC should be `Bound`

If PVC is `Pending`:

- check storage class

- check StatefulSet

- verify dynamic provisioning

---

## 6. Ingress Troubleshooting

### Check ingress resource

```bash
kubectl get ingress -n ticketing
kubectl describe ingress -n ticketing
```

Verify:

- host is correct

- backend service is correct

- ingress class is correct

---

### Problem: ingress returns 404

Possible cause:

- wrong Host header

For host-based ingress, requests must include the correct host.

Correct test:

```bash
curl -H "Host: ticketing.local" http://192.168.122.251/healthz
```

Incorrect test:

```bash
curl http://192.168.122.251/healthz
```

This may return 404 because host-based routing does not match.

---

## 7. ConfigMap and Secret Troubleshooting

### Check ConfigMap

```bash
kubectl get configmap -n ticketing
kubectl describe configmap ticketing-config -n ticketing
```

---

### Check Secret

```bash
kubectl get secret -n ticketing
kubectl describe secret ticketing-secret -n ticketing
```

---

### Common issue: wrong secret/config reference

If pod shows:

CreateContainerConfigError

Check:

```bash
kubectl describe pod <pod-name> -n ticketing
```

Typical cause:

- typo in ConfigMap or Secret name

---

## 8. Prometheus Troubleshooting

### Check Prometheus pods

```bash
kubectl get pods -n monitoring
```

Expected:

- Prometheus pods running

---

### Check scrape targets

Open Prometheus UI and go to:

Status → Targets

Expected:

- `ticketing-service` target should be `UP`

---

### If target is missing

Check:

- Prometheus scrape config

- Helm values file

- Prometheus config inside pod

Commands:

```bash
helm get values prometheus -n monitoring
kubectl get pods -n monitoring
kubectl exec -it <prometheus-pod> -n monitoring -- cat /etc/config/prometheus.yml
```

---

### If target is DOWN

Check:

- app pod readiness

- service name

- `/metrics` endpoint

Commands:

```bash
kubectl get pods -n ticketing
kubectl get svc -n ticketing
curl -H "Host: ticketing.local" http://192.168.122.251/metrics
```

---

## 9. Grafana Troubleshooting

### Check Grafana pod

```bash
kubectl get pods -n monitoring
```

---

### Check Grafana service

```bash
kubectl get svc -n monitoring
```

---

### Login issues

If login fails:

- verify admin password secret

Example:

```bash
kubectl get secret -n monitoring
```

---

### Datasource issue

If Prometheus datasource does not work:

- verify Prometheus service name

- verify Grafana datasource URL

- verify Prometheus is reachable from Grafana

---

## 10. CI/CD Troubleshooting

### Check GitHub Actions

- verify workflow ran successfully

- verify Docker image was pushed

- verify deploy step completed

---

### If deployment did not update

Check on VM:

```bash
kubectl get pods -n ticketing
kubectl rollout status deployment/ticketing-app -n ticketing
kubectl describe deployment ticketing-app -n ticketing
```

---

### If new image is not used

Verify:

- deployment image value

- image tag

- imagePullPolicy

---

## 11. Useful Commands Summary

### Application

```bash
curl -H "Host: ticketing.local" http://192.168.122.251/healthz
curl -H "Host: ticketing.local" http://192.168.122.251/readyz
curl -H "Host: ticketing.local" http://192.168.122.251/metrics
```

### Kubernetes

```bash
kubectl get pods -n ticketing
kubectl get svc -n ticketing
kubectl get ingress -n ticketing
kubectl describe pod <pod-name> -n ticketing
kubectl logs <pod-name> -n ticketing
```

### Database

```bash
kubectl exec -it postgres-0 -n ticketing -- psql -U postgres -d ticketing
kubectl get pvc -n ticketing
```

### Monitoring

```bash
kubectl get pods -n monitoring
kubectl get svc -n monitoring
helm get values prometheus -n monitoring
```

---

## 12. Escalation Pattern

If a problem occurs, check in this order:

1. ingress

2. service

3. pod

4. logs

5. environment/config

6. database

7. monitoring

This sequence helps isolate issues quickly
