import logging

from services.equipment_service import load_equipment

logger = logging.getLogger(__name__)


def initialize_startup():
     logger.info("Startup initialization started")

     equipment =  load_equipment()

     logger.info("Equipment loaded: %s", equipment)