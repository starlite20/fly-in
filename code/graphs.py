from enum import Enum

class Colors(Enum):
    GREY = "grey"
    BLUE = "blue"
    RED = "red"
    YELLOW = "yellow"
    GREEN = "green"

class Zonetype(Enum):
    NORMAL = "normal"
    RESTRICTED = "restricted"
    PRIORITY = "priority"
    BLOCKED = "blocked"


class Zone():
    # sample zone data
    # (['start', 0, 0], {'color': 'green', 'max_drones': '5'})
    def __init__(self, zone_data: tuple[list, dict]):
        self.is_start = False
        self.is_end = False

        essential, zone_metadata = zone_data

        self.set_hubname(essential[0])
        self.set_zone_coordinates(essential[1], essential[2])
        self.set_metadata(zone_metadata)

    def __str__(self):
        str_val = f"{self.hubname.capitalize()} Zone '{self.hubname}'\n"

        if self.is_start:
            str_val += "Start Hub"
        elif self.is_end:
            str_val += "End Hub"
        else:
            str_val += "Regular Hub"

        str_val += f" at {self.zone_coordinate}\n"
        str_val += "Metadata\n"
        str_val += f"-- Color : {self.color}\n"
        str_val += f"-- Max Drones : {self.max_drones}\n"
        # str_val += f"-- Max Capacity Link : {self.max_link_capacity}\n"

        return str_val

    def set_hubname(self, hubname: str):
        self.hubname = hubname
        if hubname == "start":
            self.is_start = True
        elif hubname == "end":
            self.is_end = True

    def set_zone_coordinates(self, x_val: int, y_val: int):
        self.zone_coordinate = (x_val, y_val)
    
    def set_metadata(self, metadata):
        if not metadata:
            return
        
        # color metadata
        color_str = metadata.get("color")
        if color_str:
            try:
                self.color = Colors(color_str.lower())
            except ValueError:
                raise ValueError(f"Invalid Color Value Passed -> '{color_str}'")
        else:
            self.color = Colors.GREY

        # zonetype metadata
        zone_type_str = metadata.get("zone")
        if zone_type_str:
            try:
                self.zone_type = Zonetype(zone_type_str.lower())
            except ValueError:
                raise ValueError(f"Invalid Zone Type Passed -> '{zone_type_str}'")
        else:
            self.zone_type = Zonetype.NORMAL

        # max_drones metadata
        max_drones_str = metadata.get("max_drones")
        if max_drones_str:
            try:
                self.max_drones = int(max_drones_str)
            except ValueError:
                raise ValueError(f"Invalid Value passed of Max Drones -> '{max_drones_str}'")
        else:
            self.max_drones = 1

        # max_link_capacity metadata
        # max_link_capacity_str = metadata.get("max_link_capacity")
        # if max_link_capacity_str:
        #     try:
        #         self.max_link_capacity = int(max_link_capacity_str)
        #     except ValueError:
        #         raise ValueError(f"Invalid Value passed of Max Link Capacity -> '{max_drones_str}'")
        # else:
        #     self.max_link_capacity = 1

    

