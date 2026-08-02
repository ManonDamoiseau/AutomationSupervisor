from domain.equipment import Equipment

def create_default_equipment() -> Equipment:
    return Equipment(
        name="Cyclotron",
        identifier="CYC-001",
        opcua_node_id="ns=2;s=Cyclotron.State",
    )