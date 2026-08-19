import re

line1 = "hub: waypoint1 1 0 [color=blue]"
pattern = r"^(start_hub|end_hub|hub):\s+(\w+)\s+(-?\d+)\s+(-?\d+)(?:\[(.*)\])?$"

match = re.match(pattern, line1)
if match:
    print("Match successful!")
    print("Extracted Data:", match.groups())
else:
    print("No match found.")