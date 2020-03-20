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

# x = session.query(Region).filter(Region.name=="Mauricie").first()

# data = np.genfromtxt("results.csv", delimiter=',')
# x.coordinates = data.tolist()
# session.add(x)
# session.commit()

for x in session.query(Region):
	print(x.id, x.name)