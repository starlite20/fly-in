from zones import Zone


class Connection():
    def __init__(self, zone_a: Zone, zone_b: Zone, max_link_capacity: int = 1):
        self.zone_a = zone_a
        self.zone_b = zone_b
        self.max_link_capacity = max_link_capacity

    def __str__(self):
        str_val = ""
        str_val += f"-- Max Capacity Link : {self.max_link_capacity}\n"
        return str_val
