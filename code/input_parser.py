
class InputParser():
    _MANDATORY_KEYS = ["nb_drones", "start_hub", "end_hub", "connection"]
    _OPTIONAL_KEYS = ["hub"]
    _ALL_KEYS = _MANDATORY_KEYS + _OPTIONAL_KEYS
    _VALID_METADATA_KEYS = ["color", "zone", "max_drones", "max_link_capacity"]

    def __init__(self, filename: str):
        self._filename = filename
        self._nb_drones = -1
        self._start_hub_str = []
        self._end_hub_str = []
        self._all_hubs_str = []
        self._all_connections_str = []

    def __str__(self):
        return (
            f"Filename \t\t: '{self._filename}'\n"
            f"Number of Drones \t\t: '{self._nb_drones}'\n"
            f"Start Hub Data \t\t: '{self._start_hub_str}'\n"
            f"End Hub Data \t\t: '{self._end_hub_str}'\n"
            f"Hubs Data \t\t: '{self._all_hubs_str}'\n"
            f"Connections Data \t\t: '{self._all_connections_str}'\n"
        )

    def parse_file(self) -> None:
        with open(self._filename, 'r') as file:
            for line_num, line in enumerate(file, start=1):
                self._process_data_line(line_num, line)

        self._validate_mandatory()

    def _process_data_line(self, line_num: int, line: str) -> None:
        line = line.strip()
        if ((not line)
            or (':' not in line)
                or (line.startswith('#'))):
            return

        lhs = ""
        rhs = ""
        try:
            lhs, rhs = line.split(': ', 1)
        except ValueError:
            raise ValueError(
                f"Line {line_num} is in the wrong formatting with content '{line}'")

        if lhs == "nb_drones":
            self._set_nb_drones(rhs)
        elif lhs == "connection":
            self._set_connection(rhs)
        elif lhs == "start_hub":
            self._set_start_hub(rhs)
        elif lhs == "end_hub":
            self._set_end_hub(rhs)
        elif lhs == "hub":
            self._set_hub(rhs)
        else:
            raise ValueError(f"Invalid Key passed in Input -> '{lhs}'")

    def _set_nb_drones(self, value: str) -> None:
        if self._nb_drones != -1:
            raise ValueError(
                f"Multiple Values passed for nb_drones -> '{value}'")
        try:
            self._nb_drones = int(value)
        except ValueError:
            raise ValueError(
                f"nb_drones must have an integer value. Value passed in -> '{value}'")

    def _set_start_hub(self, value: str) -> None:
        extracted_val = self._extract_components(value)
        self._start_hub_str.append(extracted_val)

    def _set_end_hub(self, value: str) -> None:
        extracted_val = self._extract_components(value)
        self._end_hub_str.append(extracted_val)

    def _set_connection(self, value: str) -> None:
        extracted_val = self._extract_components(value, "connection")
        self._all_connections_str.append(extracted_val)

    def _set_hub(self, value: str) -> None:
        extracted_val = self._extract_components(value)
        self._all_hubs_str.append(extracted_val)

    def _validate_mandatory(self):
        if self._nb_drones == -1:
            raise ValueError("Missing value for nb_drones")

        elif len(self._start_hub_str) > 1:
            raise ValueError("Too many start zones provided.")
        elif len(self._start_hub_str) < 1:
            raise ValueError("Missing value for start zones.")

        elif len(self._end_hub_str) > 1:
            raise ValueError("Too many end zones provided.")
        elif len(self._end_hub_str) < 1:
            raise ValueError("Missing value for end zones.")

    def _extract_components(self, raw_str: str, data_type: str = "zone"):
        # print(raw_str)
        # sample raw str
        # 'start 0 0 [color=green]'

        if data_type == "zone":
            # check if metadata given
            if '[' in raw_str:
                essential_str, metadata_str = raw_str.split(' [', 1)
                metadata_str = metadata_str.rstrip(']').strip()
            else:
                essential_str = raw_str
                metadata_str = ""

            # process essential values for zones
            essential = essential_str.split(' ')
            if len(essential) != 3:
                raise ValueError(
                    "Zones must be declared in the format '<hub_type>: <name> <x_coord> <y_coord> [<metadata_key>=<metadata_value> ...]'")
            try:
                x_coord = int(essential[1])
                y_coord = int(essential[2])
            except ValueError:
                raise ValueError(
                    f"X,Y Coordinates must be a valid integer value. Invalid values provided : {essential[1]}, {essential[2]}")
            essential_list = [essential[0], x_coord, y_coord]

            # process metadata part
            metadata = {}
            if metadata_str:
                for mdata in metadata_str.split(' '):
                    if '=' not in mdata:
                        raise ValueError(
                            "Metadata must be in format '[<key>=<value ...]'")

                    key, val = mdata.split('=', 2)

                    if key not in self._VALID_METADATA_KEYS:
                        raise ValueError(
                            f"Invalid metadata key passed -> '{key}'")
                    metadata[key] = val

            print()
            print(
                f" essential '{essential_list}'    +   metadata '{metadata}'")

            return (essential_list, metadata)

        elif data_type == "connection":
            edge_one, edge_two = raw_str.split('-', 1)
            if '-' in edge_two:
                raise ValueError(
                    "Connections must be declared in the format 'connection: <zone_1_name>-<zone_2_name>'")
            print()
            print(f"extracting edge --{edge_one}-- --{edge_two}--")
            return (edge_one, edge_two)
            pass
