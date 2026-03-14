import logging
import time

from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware

from app.api.routes.health import router as health_router
from app.api.routes.tickets import router as tickets_router
from app.api.routes.metrics import (
    router as metrics_router,
    REQUEST_COUNT,
    REQUEST_LATENCY,
)
from app.core.config import settings
from app.core.logging import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

app = FastAPI(title=settings.app_name)


class MetricsMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()

        response = await call_next(request)

        duration = time.time() - start_time
        endpoint = request.url.path
        method = request.method
        status_code = str(response.status_code)

        REQUEST_COUNT.labels(method=method, endpoint=endpoint, status=status_code).inc()
        REQUEST_LATENCY.labels(method=method, endpoint=endpoint).observe(duration)

        return response


app.add_middleware(MetricsMiddleware)

app.include_router(health_router)
app.include_router(tickets_router)
app.include_router(metrics_router)


@app.on_event("startup")
def startup_event():
    logger.info("Application startup complete")
