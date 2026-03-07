import logging
from fastapi import FastAPI
from app.api.routes.health import router as health_router
from app.api.routes.tickets import router as tickets_router
from app.core.config import settings
from app.core.logging import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

app = FastAPI(title=settings.app_name)

app.include_router(health_router)
app.include_router(tickets_router)


@app.on_event("startup")
def startup_event():
    logger.info("Application startup complete")