import os
import requests
from bs4 import BeautifulSoup

class CovidScraper:

	def __init__(self):
		self.page = requests.get(os.environ.get("QUEBEC_GOVT_WEBSITE"))
		self.soup = BeautifulSoup(self.page.content, 'html.parser')
		self.htmltable = self.soup.find('table', { 'class' : 'contenttable' })
		self.rows = self.htmltable.find_all("tr")
		self.montreal_cases = -1
		self.quebec_prov_cases = -1
		# print(self.page.text)
		# print(self.soup.text)
		# print(self.htmltable.text)
		for row in self.rows:
			row_list = row.find_all("td")
			# print(row_list)
			if len(row_list)>=2:
				if "Montr" in row_list[0].text:
					self.montreal_cases = int(row_list[1].text)
				elif "Total" in row_list[0].text:
					self.quebec_prov_cases = int(row_list[1].text)

	def return_values(self):
		return_dict = {"montreal_cases":self.montreal_cases, "quebec_prov_cases":self.quebec_prov_cases}
		return return_dict