from config.database import engine
from config.logger import logger
from config.settings import settings

logger.info("Application Started")

print(settings.DATABASE_URL)

with engine.connect() as conn:
    print("✅ Database Connected Successfully")

logger.info("Application Finished")
