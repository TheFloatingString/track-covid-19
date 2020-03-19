import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from db.models import TransitLine

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

engine = create_engine(os.environ["DATABASE_URL"], echo = True)

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

line = TransitLine()
# line.create_entry(name="STM 106",
# 	alert=True,
# 	coordinates=[[]],
# 	description="""106 bus from boulevard Newman toward Angrignon metro station	March 10, between 10:40 a.m. and 10:50 a.m.	March 24, 2020""")
# session.add(line)
# session.commit()