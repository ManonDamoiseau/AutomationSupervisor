from domain.equipment import Equipment
from services.configuration_service import load_equipment_configuration

def load_equipment() -> list[Equipment]:
    """
    Load equipment definitions from configuration
    and create domain Equipment objects.

    Returns:
        list[Equipment]: List of configured equipments.
    """
      
    configuration = load_equipment_configuration() #reading YAML
    equipment_configs = configuration ["equipment"] #returns the value associated with the equipment key in the configuration dictionary

    equipments = [] # Create the business list

    for config in equipment_configs: # Business transformation, dictionary --> object
        equipment = Equipment(
            name=config["name"],
            identifier=config["identifier"],
            opcua_node_id=config["opcua_node_id"],
        )

        equipments.append(equipment)

    return equipments