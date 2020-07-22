import json
from datetime import datetime

class DataFileManager:
	
	def __init__(self, json_file_name = None):
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

		self.holder[name].insert(0 ,{'date' : today(),'cost': price, 'coins': coins })
		
	def dump(self, filename):
		file = open(filename, 'w')
		json.dump(self.holder,file,indent='\t')
		
		
class Holder:
	def __init__(self):
		self.master_list = {}
		
	def addDollars(self, name, dollars):
		if name not in self.master_list:
			self.master_list[name] = {'coins': 0, 'dollars': dollars}
		else:
			self.master_list[name]['dollars'] = dollars
			
	def addCoins(self, name, coins):
		if name not in self.master_list:
			self.master_list[name] = {'coins': coins, 'dollars': 0.00}
		else:
			self.master_list[name]['coins'] = coins
			
	def dumpDict(self):
		copy = self.master_list.copy()
		self.master_list = {}
		return copy
		
		
			
def today():
	return str(datetime.date(datetime.now()))