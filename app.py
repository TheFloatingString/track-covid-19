import os

from src import webscrape_data
from db.models import TransitLine

from flask import Flask, render_template
from flask_cors import CORS, cross_origin

from sqlalchemy	import create_engine
from sqlalchemy.orm import sessionmaker


app = Flask(__name__)

scraper = webscrape_data.CovidScraper()

engine = create_engine(os.environ["DATABASE_URL"], echo = True)

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()


@cross_origin()
@app.route("/")
def home():
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

if __name__ == '__main__':
	app.run(debug=True)