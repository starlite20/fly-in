import re

#test regex

# line1 = "hub: waypoint1 1 0 [color=blue]"
line1 = "hub: final_torture2 18 0 [color=crimson max_drones=1]"
pattern = r"^(start_hub|end_hub|hub):\s+(\w+)\s+(-?\d+)\s+(-?\d+)\s*(?:\[(.*)\])?$"

match = re.match(pattern, line1)

print(f"\nline : {line1}")
print(f"pattern : {pattern}")
if match:
    print("Match successful!")
    print("Extracted Data:", match.groups())
else:
    print("No match found.")