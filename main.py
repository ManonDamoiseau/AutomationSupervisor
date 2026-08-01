import logging

from config.settings import APPLICATION_NAME, PLC_IP, PLC_PORT
from logging_config import configure_logging
from services.startup import initialize_startup 

logger = logging.getLogger(__name__)

configure_logging()
logger.info("Application is starting")
initialize_startup()
logger.info(f"Application: {APPLICATION_NAME}")
logger.info(f"PLC IP   : {PLC_IP}")
logger.info(f"PLC PORT : {PLC_PORT}")
