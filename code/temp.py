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

    def _initiate_zones(self, role: Zonerole, hubs_list: list) -> None:
        for hub_data in hubs_list:
            zone = Zone(role, hub_data)

            # Dictionary duplicate check is O(1)
            if zone.zone_name in self.zones:
                raise ValueError(
                    f"Duplicate zone name found: '{zone.zone_name}'")

            # Dictionary assignment is O(1)
            self.zones[zone.zone_name] = zone

    def _get_zone(self, zone_name: str) -> Zone:
        # Dictionary lookup is O(1). No for-loops needed.
        zone = self.zones.get(zone_name)
        if zone is None:
            raise ValueError(
                f"Connection references undefined zone: '{zone_name}'")
        return zone

    def _initiate_connections(self, connections_list: list) -> None:
        for conn_data in connections_list:
            essential, metadata = connection

            # Directly fetch the objects using the O(1) dictionary
            zone_a = self._get_zone(essential[0])
            zone_b = self._get_zone(essential[1])

            max_capacity = 1
            max_capacity_str = metadata.get("max_link_capacity")
            if max_capacity_str:
                try:
                    max_capacity = int(max_capacity_str)
                except ValueError:
                    raise ValueError(
                        f"Invalid value for max_link_capacity -> '{max_capacity_str}'")

            self.connections.append(Connection(zone_a, zone_b, max_capacity))
