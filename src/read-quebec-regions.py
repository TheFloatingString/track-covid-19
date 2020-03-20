import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import json

from db.models import Region

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

engine = create_engine(os.environ["DATABASE_URL"], echo = True)

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

with open("data/regions_quebec.geojson", 'r') as f:
	data = json.load(f)


def fixes(string):
	string = string.replace("Ã©", "é")
	string = string.replace("ÃŽ", "Î")
	string = string.replace("Ã¨", "è")
	string = string.replace("Ã´", "ô")

	return string

session.query(Region).delete()
session.commit()

for region in data["features"]:
	print(fixes(region["properties"]["res_nm_reg"]))
	# print(len(region["geometry"]["coordinates"]))
	name = fixes(region["properties"]["res_nm_reg"])
	coordinates = []
	final_coordinates = []
	if "e-Nord" in fixes(region["properties"]["res_nm_reg"]):
		coordinates = [region["geometry"]["coordinates"][0]]
	else:
		coordinates = region["geometry"]["coordinates"]


	for row in coordinates[0][0]:
		# print(row)
		final_coordinates.append(list(reversed(row)))
		# break
	region = Region()
	region.create_region(name, final_coordinates)
	print(region.name)
	print()
	session.add(region)
	session.commit()