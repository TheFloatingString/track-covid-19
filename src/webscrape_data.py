import os
import sys
import requests
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from bs4 import BeautifulSoup

from sqlalchemy	import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import Region


engine = create_engine(os.environ["DATABASE_URL"], echo = False)

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()


# for x in session.query(Region):
	# print(x.uuid, x.name)

class CovidScraper:

	def __init__(self):
		self.page = requests.get(os.environ.get("QUEBEC_GOVT_WEBSITE"))
		self.soup = BeautifulSoup(self.page.content, 'html.parser')
		self.htmltable = self.soup.find('table', { 'class' : 'contenttable' })
		self.rows = self.htmltable.find_all("tr")
		self.montreal_cases = -1
		self.quebec_prov_cases = -1
    

	def return_values(self):

		return_dict = dict()
		return_dict["data"] = dict()
		return_dict["data"]["administrative_regions"] = dict()
		return_dict["data"]["provinces"] = dict()

		# print(self.rows)
		for row in self.rows:
			# print(row)
			row_list = row.find_all("td")
			# print(row_list)
			# print()
			if len(row_list)>=2 and ' - ' in row_list[0].text:

				admin_region_name = row_list[0].text.split(' - ')[1].replace(' ','-')
				number_of_cases = int(row_list[1].text)
				print(row_list[0].text)

				x = session.query(Region).filter(Region.name == admin_region_name).first()
				print(x.name, len(x.coordinates))

				element_dict = {"name":admin_region_name, 
				"cases":number_of_cases,
				"coordinates":x.coordinates,
				"population":x.population,
				"case-per-pop":int(round(x.population/number_of_cases)),
				"case-percent":round(number_of_cases/x.population*100, 6)}

				# print(return_dict["data"]["administrative_regions"])
				return_dict["data"]["administrative_regions"][admin_region_name] = element_dict

				# if ' - ' in str(row_list[0].text):
				# 	print(row_list[0].text.split(' - ')[1])
				# if "Montr" in row_list[0].text:
				# 	self.montreal_cases = int(row_list[1].text)
				# elif "Total" in row_list[0].text:
				# 	self.quebec_prov_cases = int(row_list[1].text)

			elif len(row_list)>=2 and "Total" in row_list[0].text:
				print(type(row_list[1].text))
				print(row_list[1].text.replace('\xa0', ''))
				return_dict["data"]["provinces"]["Québec"] = {"name":"Québec", "cases":int(row_list[1].text.replace('\xa0', ''))}

		return return_dict

if __name__ == '__main__':
	for x in session.query(Region):
		print(x.id, x.name)
	scraper = CovidScraper()
	scraper.return_values()
	# print(scraper.return_values())

