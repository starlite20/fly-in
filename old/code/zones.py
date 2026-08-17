from enum import Enum


class Zonerole(Enum):
    START = "start_hub"
    END = "end_hub"
    HUB = "hub"


class Zonetype(Enum):
    NORMAL = "normal"
    RESTRICTED = "restricted"
    PRIORITY = "priority"
    BLOCKED = "blocked"


class Zone():
    # sample zone data
    # (['start', 0, 0], {'color': 'green', 'max_drones': '5'})
    def __init__(self, role: Zonerole, zone_data: tuple[list, dict]):
        self.role = role
        self.is_start = (role == Zonerole.START)
        self.is_end = (role == Zonerole.END)

        essential, zone_metadata = zone_data

        self.zone_name = essential[0]
        self.zone_coordinate = (essential[1], essential[2])
        self.set_metadata(zone_metadata)

    def __str__(self):
        str_val = f"{self.zone_name.capitalize()} Zone '{self.zone_name}'\n"
        str_val += f"{self.role} at {self.zone_coordinate}\n"
        str_val += "Metadata\n"
        str_val += f"-- Color : {self.color}\n"
        str_val += f"-- Max Drones : {self.max_drones}\n"
        return str_val

    def set_metadata(self, metadata):
        # color metadata
        self.color = metadata.get("color", "none")

        # zonetype metadata
        zone_type_str = metadata.get("zone")
        if zone_type_str:
            try:
                self.zone_type = Zonetype(zone_type_str.lower())
            except ValueError:
                raise ValueError(
                    f"Invalid Zone Type Passed -> '{zone_type_str}'")
        else:
            self.zone_type = Zonetype.NORMAL

        # max_drones metadata
        max_drones_str = metadata.get("max_drones")
        if max_drones_str:
            try:
                self.max_drones = int(max_drones_str)
            except ValueError:
                raise ValueError(
                    f"Invalid Value passed of Max Drones -> '{max_drones_str}'")
        else:
            self.max_drones = 1
