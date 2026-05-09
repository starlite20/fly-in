from input_parser import InputParser

try:
    inputconfig = InputParser("testtext.txt")
    inputconfig.parse_file()
    print()
    print(inputconfig)
except Exception as e:
    print(f"Error: {e}")
