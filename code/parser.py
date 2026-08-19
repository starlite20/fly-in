import re
from models import Zone, ZoneType, Connection


def parse_map(filepath: str):
	#using regex to parse