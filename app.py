import os

from src import webscrape_data
from db.models import TransitLine, View, Location, Anxiety

from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin

from sqlalchemy	import create_engine
from sqlalchemy.orm import sessionmaker


app = Flask(__name__)

scraper = webscrape_data.CovidScraper()

engine = create_engine(os.environ["DATABASE_URL"], echo = True)

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
session.rollback()

@cross_origin()
@app.route("/")
def home():
	# view = View()
	# view.create_view()
	# session.add(view)
	# session.commit()
	return render_template("home.html")

@cross_origin()
@app.route("/get_cases", methods=["GET"])
def get_cases():
	values = scraper.return_values()
	return values

@cross_origin()
@app.route("/get_coordinates", methods=["GET"])
def get_coords():
	return_dict = dict()
	return_dict["data"] = []
	for line in session.query(TransitLine):
		dict_item = dict()
		dict_item["name"] = line.name
		dict_item["coordinates"] = line.coordinates
		dict_item["description"] = line.description
		return_dict["data"].append(dict_item)
	return return_dict

@app.route("/contact")
def contact():
	return render_template("contact.html")

@app.route("/post_location", methods=["GET", "POST"])
def post_location():
	# print("post_location")
	# print(request.form)
	# print(request.form.get("name"))
	# print(request.form.get("description"))

	location = Location()
	location.create_location(name=request.form["name"], 
		address=request.form["address"], 
		description=request.form["description"],
		contact=request.form["contact"])

	session.add(location)
	session.commit()

	return str(request.form)

@app.route("/post_anxiety", methods=["GET", "POST"])
def post_anxiety():
	print('post_anxiety')
	print(request.form)
	anxiety = Anxiety()
	anxiety.create(dict_description=request.form)
	session.add(anxiety)
	session.commit()
	print("done!")
	return "Done"

if __name__ == '__main__':
	for x in session.query(Anxiety):
		print(x.id, x.dict_description)
	app.run(debug=True)