import sys
import os

import numpy as np

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import json

from db.models import Region

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

engine = create_engine(os.environ["DATABASE_URL"], echo = True)

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

for region in session.query(Region):
	print(region.id, region.uuid, region.name)


# x = session.query(Region).filter(Region.uuid=="a2c7a89e-7848-43d4-a3c9-105ea77b4e58").first()

# # data = np.genfromtxt("results.csv", delimiter=',')
# x.name = "Saguenay–Lac-Saint-Jean"
# # x.coordinates = data.tolist()
# session.add(x)
# session.commit()

# upgrade_list = [[85,276368],
# 			[87,146717],
# 			[84,382604],
# 			[86,90311],
# 			[88,266112+242399],
# 			[89,729997],
# 			[90,589400],
# 			[91,420082],
# 			[92,494796],
# 			[93,1507070],
# 			[94,319004],
# 			[95,44561],
# 			[96,1942044],
# 			[97,92518],
# 			[98,197385],
# 			[99,422993],
# 			[100,242399]]

# for row in upgrade_list:
# 	x = session.query(Region).filter(Region.id==row[0]).first()
# 	x.population = row[1]
# 	session.add(x)
# 	session.commit()

# x = session.query(Region).filter(Region.uuid=="763b6a9f-2776-477b-8cc0-ffba3d61a611").first()

# # data = np.genfromtxt("results.csv", delimiter=',')
# x.name = "Abitibi-Temiscamingue"
# # x.coordinates = data.tolist()
# session.add(x)
# session.commit()

for x in session.query(Region):
	print(x.id, x.name, x.population)
