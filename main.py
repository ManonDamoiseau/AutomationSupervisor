import logging

from config.settings import APPLICATION_NAME, PLC_IP, PLC_PORT
from logging_config import configure_logging

configure_logging()
logging.info("Application is starting")
logging.info(f"Application: {APPLICATION_NAME}")
logging.info(f"PLC IP   : {PLC_IP}")
logging.info(f"PLC PORT : {PLC_PORT}")
