# System Architecture



```markdown
# System Architecture

```mermaid
flowchart LR
    Client[Client / User] --> Ingress[Ingress]
    Ingress --> Service[Ticketing Service]
    Service --> App[FastAPI Application]
    App --> DB[(PostgreSQL)]
```
