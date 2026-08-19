from enum import Enum
from dataclasses import dataclass


class ZoneType(Enum):
    NORMAL = "normal"
    RESTRICTED = "restricted"
    PRIORITY = "priority"
    BLOCKED = "blocked"

@dataclass
class Zone:
    name: str
    x: int
    y: int
    zone_type: ZoneType = ZoneType.NORMAL
    color: str = "none"
    max_drones: int = 1
    is_start: bool = False
    is_end: bool = False


@dataclass
class Connection:
    node_a: str
    node_b: str
    max_link_capacity: int = 1