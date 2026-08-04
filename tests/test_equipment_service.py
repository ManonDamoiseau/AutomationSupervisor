from services.equipment_service import load_equipment

def test_load_equipment_returns_configured_equipments():
    equipments = load_equipment()

    assert len(equipments) == 4

    cyclotron = next(
        (
            equipment
            for equipment in equipments
            if equipment.identifier == "CYC-001"
        ),
        None
    )

    assert cyclotron is not None
    
    assert cyclotron.name == "Cyclotron"
    assert cyclotron.opcua_node_id == "ns=2;s=Cyclotron.Status"
