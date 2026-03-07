import logging
from pythonjsonlogger import jsonlogger
from app.core.config import settings


def setup_logging() -> None:
    logger = logging.getLogger()
    logger.setLevel(settings.log_level)

    logger.handlers.clear()

    handler = logging.StreamHandler()
    formatter = jsonlogger.JsonFormatter(
        "%(asctime)s %(levelname)s %(name)s %(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)