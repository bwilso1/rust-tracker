
class item:
	def __init__(self, name, quantity_available, price):
		self.name = name
		self.quantity = quantity_available
		self.price = price
		
	def __str__(self):
		return "name: %s\t avail: %s\t price: %s" % (self.name, self.quantity,self.price)
	
	def __repr__(self):
		return self.__str__()