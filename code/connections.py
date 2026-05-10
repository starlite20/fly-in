class Connection():
    def __init__(self, zone_a_name: str, zone_b_name: str, max_link_capacity: int = 1):
        self.zone_a_name = zone_a_name
        self.zone_b_name = zone_b_name
        self.max_link_capacity = max_link_capacity

    def __str__(self):
        str_val = ""
        str_val += f"-- Max Capacity Link : {self.max_link_capacity}\n"
        return str_val
