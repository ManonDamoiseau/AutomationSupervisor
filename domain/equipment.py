from dataclasses import dataclass

@dataclass
class Equipment:
    """
    Represents an industrial equipment monitored by the Automation Supervisor
    """

    name: str
    identifier: str
    opcua_node_id:str 