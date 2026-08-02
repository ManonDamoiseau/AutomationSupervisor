import logging

from services.equipment_service import create_default_equipment

logger = logging.getLogger(__name__)


def initialize_startup():
     logger.info("Startup initialization started")

     equipment = create_default_equipment()

     logger.info("Equipment created: %s", equipment)