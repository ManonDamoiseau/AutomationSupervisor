from services.equipment_service import create_default_equipment

def test_create_default_equipment_returns_expected_equipment():
    equipment = create_default_equipment()

    assert equipment.name == "Cyclotron"
    assert equipment.identifier == "CYC-001"
    assert equipment.opcua_node_id == "ns=2;s=Cyclotron.State"