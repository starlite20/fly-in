def read_file(filename: str):
    with open(filename) as file:
        data = file.readline()
        while (data):
            print(data)
            data = file.readline()
