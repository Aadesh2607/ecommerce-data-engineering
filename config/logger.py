"""
Central logging configuration.
"""

import logging
from pathlib import Path

from config.settings import settings

settings.LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = Path(settings.LOG_DIR) / "pipeline.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler(),
    ],
)

logger = logging.getLogger("ecommerce_pipeline")
