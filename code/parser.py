import re
from models import Zone, ZoneType, Connection


def parse_map(filepath: str):
	#regex
	# hub: roof1 3 4 [zone=restricted color=red]
	# starts with hub / starthub / endhub
	# next : some space
	# nest : 

	# ^(start_hub|end_hub|hub):\s+(\w+)\s+((\+|-)?\d)+\s+((\+|-)?\d+)(\[[0-9a-z]\=[0-9a-z])+\])?