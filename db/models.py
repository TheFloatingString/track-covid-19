from sqlalchemy import Table, Column, Integer, Float, String, MetaData, DateTime, Boolean
from sqlalchemy.types import ARRAY
from sqlalchemy	import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
import os

from werkzeug.security import generate_password_hash, check_password_hash

# from src import read_credentials

import bcrypt
from uuid import uuid4
import random
import datetime


# env_keys = read_credentials.return_keys()

engine = create_engine(os.environ["DATABASE_URL"], echo = True)

meta = MetaData()
Base = declarative_base()


class TransitLine(Base):
	__tablename__ = "transit_lines"

	id = Column(Integer, primary_key=True, autoincrement=True)
	uuid = Column(UUID(as_uuid=True), default=uuid4)
	name = Column(String)
	alert = Column(Boolean)
	coordinates = Column(ARRAY(Float))
	description = Column(String)
	date_created = Column(DateTime)
	date_modified = Column(DateTime)

	def create_entry(self, name, alert, coordinates, description):
		self.name = name
		self.alert = alert
		self.coordinates = coordinates
		self.description = description
		self.date_created = datetime.datetime.now()
		self.date_modified = datetime.datetime.now()

	def __repr__(self):
		return "<TransitLine(uuid='%s', name='%s')>" %(self.uuid, self.name)


class Location(Base):
	__tablename__ = "locations"

	id = Column(Integer, primary_key=True, autoincrement=True)
	uuid = Column(UUID(as_uuid=True), default=uuid4)
	name = Column(String)
	category = Column(ARRAY(String))	# categories: ['business', 'test_centre']
	creator_id = Column(UUID)
	coordinates = Column(ARRAY(Float))
	population = Column(Integer)
	address = Column(String)
	description = Column(String)
	contact = Column(String)
	update_ids = Column(ARRAY(UUID))
	date_created = Column(DateTime)
	date_modified = Column(DateTime)

	def create_location(self, name, address=None, description=None, contact=None):
		self.name = name 
		self.address = address
		self.description = description
		self.contact = contact
		self.date_created = datetime.datetime.now()
		self.date_modified = datetime.datetime.now()	


class LocationUpdate(Base):
	__tablename__ = "location_updates"

	id = Column(Integer, primary_key=True, autoincrement=True)
	uuid = Column(UUID(as_uuid=True), default=uuid4)
	location_uuid = Column(UUID)
	user_uuid = Column(UUID)
	description = Column(String)

	def create_update(self, location_uuid, user_uuid, description):
		self.location_uuid = location_uuid
		self.user_uuid = user_uuid
		self.description = description

class User(Base):
	__tablename__ = "users"

	id = Column(Integer, primary_key=True, autoincrement=True)
	uuid = Column(UUID(as_uuid=True), default=uuid4)
	first_name = Column(String)
	last_name = Column(String)
	password_hash = Column(String)
	email = Column(String)
	description = Column(String)
	date_created = Column(DateTime)
	date_modified = Column(DateTime)

	def create_user(self, first_name, last_name, email, password, description=None):
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
		self.description = description
		self.date_created = datetime.datetime.now()
		self.date_modified = datetime.datetime.now()	


class View(Base):
	__tablename__ = "views"

	id = Column(Integer, primary_key=True, autoincrement=True)
	uuid = Column(UUID(as_uuid=True), default=uuid4)
	date_created = Column(DateTime)
	date_modified = Column(DateTime)	

	def create_view(self):
		self.date_created = datetime.datetime.now()
		self.date_modified = datetime.datetime.now()	


class Region(Base):
	__tablename__ = "regions"

	id = Column(Integer, primary_key=True, autoincrement=True)
	uuid = Column(UUID(as_uuid=True), default=uuid4)
	name = Column(String)
	coordinates = Column(ARRAY(Float))
	cases = Column(Integer)
	recoveries = Column(Integer)
	fatalities = Column(Integer)
	description = Column(String)
	date_created = Column(DateTime)
	date_modified = Column(DateTime)

	def create_region(self, name, coordinates):
		self.name = name
		self.coordinates = coordinates
		self.date_created = datetime.datetime.now()
		self.date_modified = datetime.datetime.now()	

	def update_numbers(self, cases, recoveries, fatalities):
		self.cases = cases
		self.recoveries = recoveries
		self.fatalities = fatalities
		self.date_modified = datetime.datetime.now()

	def update_description(self, description):
		self.description = description

	def __repr__(self):
		return "<Region(uuid='%s', name='%s', cases='%s')>" %(self.uuid, self.name, self.cases)

if __name__ == "__main__":
	Base.metadata.create_all(engine)