from input_parser import InputParser

from graph import Graph


inputconfig = None
try:
    inputconfig = InputParser("testtext.txt")
    inputconfig.parse_file()
    print()
    print(inputconfig)
except Exception as e:
    print(f"Error: {e}")


if inputconfig is not None:
    graph = Graph(inputconfig)
