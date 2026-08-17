from input_parser import InputParser
from zones import Zone, Zonerole
from connections import Connection


class Graph():
    def __init__(self, input_values: InputParser):
        self._nb_drones = input_values.nb_drones
        self.zones: dict[str, Zone] = {}
        self.connections: list[Connection] = []

        self._initiate_zones(Zonerole.START, input_values.start_hub_str)
        self._initiate_zones(Zonerole.END, input_values.end_hub_str)
        self._initiate_zones(Zonerole.HUB, input_values.all_hubs_str)

        self._initiate_connections(input_values.all_connections_str)


    def __str__(self):
        # to be updated later
        return ""

    def _initiate_zones(self, role: Zonerole, hubs_list: list):
        for hub_data in hubs_list:
            zone = Zone(role, hub_data)

            if zone.zone_name in self.zones:
                raise ValueError(f"Duplicate zone name found: '{zone.zone_name}'")
            # hash mapping dictionary
            self.zones[zone.zone_name] = zone

    def _get_zone(self, find_zone_name: str) -> Zone:
        zone = self.zones.get(find_zone_name)

        if zone is None:
            raise ValueError(f"Connection references undefined zone: '{find_zone_name}'")
        
        return zone

    def _initiate_connections(self, connections_list: list) -> None:
        for conn_data in connections_list:
            essential, metadata = conn_data

            zone_a = self._get_zone(essential[0])
            zone_b = self._get_zone(essential[1])
            
            max_link_capacity = 1
            max_link_capacity_str = metadata.get("max_link_capacity")
            if max_link_capacity_str:
                try:
                    max_link_capacity = int(max_link_capacity_str)
                except ValueError:
                    raise ValueError(
                        f"Invalid Value passed of max_link_capacity -> '{max_link_capacity_str}'")

            self.connections.append(Connection(
                zone_a, zone_b, max_link_capacity))
