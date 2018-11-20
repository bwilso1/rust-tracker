import json
from datetime import datetime

class DataManager:
	
	def __init__(self,json_file_name = None):
		if json_file_name:
			try:
				file = open(json_file_name,'r')
				self.holder = json.load(file)
			except FileNotFoundError:
				self.holder = {}
		else:
			self.holder = {}
		
	def add(self,name,price,coins):
		if name not in self.holder:
			self.holder[name] = []

		self.holder[name].append({'date' : today(),'cost': price, 'coins': coins })
		
	def dump(self, filename):
		file = open(filename, 'w')
		json.dump(self.holder,file,indent='\t')
		
			
			
def today():
	return str(datetime.date(datetime.now()))