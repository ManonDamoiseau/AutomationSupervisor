from pathlib import Path

import yaml


def load_equipment_configuration() -> dict:
    """
    Load the equipment configuration from the YAML file.

    Returns:
        dict: Complete application configuration loaded from YAML.
    """

    config_file = Path("config") / "equipment.yaml"

    with config_file.open("r", encoding="utf-8") as file:
        configuration = yaml.safe_load(file)

    return configuration