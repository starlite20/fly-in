
def read_file(filename: str):
    MANDATORY_KEYS = ["nb_drones", "start_hub", "hub", "end_hub", "connection"]
    valid_data = True
    essential_keys = {}
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if (not line) or (":" not in line) or (line.startswith("#")):
                continue
            lhs, rhs = line.split(": ", 2)
            if (lhs not in MANDATORY_KEYS):
                # error here
                valid_data = False
                raise ValueError(f"INVALID KEY FOUND : {lhs}")

            essential_keys.setdefault(lhs, []).append(rhs.split(' '))
            line = file.readline()

    if (valid_data):
        print(essential_keys)
