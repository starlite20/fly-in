from input_parser import read_file

try:
    read_file("testtext.txt")
except Exception as e:
    print(f"Error: {e}")
