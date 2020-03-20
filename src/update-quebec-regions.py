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

for region in session.query(Region):
	print(region.id, region.uuid, region.name)

x = session.query(Region).filter(Region.uuid=="b8f57cc0-52e7-4511-9b9d-fc4a3432489e").first()
print(x)