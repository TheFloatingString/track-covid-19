from flask import Flask, render_template
from src import webscrape_data
from flask_cors import CORS, cross_origin


app = Flask(__name__)

scraper = webscrape_data.CovidScraper()

@cross_origin()
@app.route("/")
def home():
	values = scraper.return_values()
	print(values)
	return render_template("home.html")

@cross_origin()
@app.route("/get_cases", methods=["GET"])
def get_cases():
	values = scraper.return_values()
	return values

if __name__ == '__main__':
	app.run(debug=True)