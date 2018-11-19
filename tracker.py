import inspect
import requests
from bs4 import BeautifulSoup
from time import sleep
from item import *
import json

#NOTES:
#		timeout seems to be 60 seconds, server side


URL = "https://steamcommunity.com/market/search?appid=252490&q="
querys = ['unknown+territory+hoodie','mp5']
#SKIN_EARN_LINK = "https://skinearn.com/api/shop?orderBy=price&order=DESC&game_id=5&name=%s&offset=%s&limit=%s" % ('mp5',0,'9')
SKIN_EARN_LINK = "https://skinearn.com/api/shop?orderBy=price&order=DESC&game_id=5&name=%s&offset=%s&limit=%s"
local = False

def launch():
	
	if local:
		file = open('sample2.htm',encoding='utf-8')
		soup = BeautifulSoup(file)
	else:
		page = requests.get(URL + querys[1])
		soup = BeautifulSoup(page.text,'html5lib')
	

	
	all_divs = soup.find_all('a', {'class':"market_listing_row_link"})
	
	results = []
	for div in all_divs:
		results.append(breakdown(div))
	print("getting steam items\n")
	for x in results:
		print(x)
		
	page2 = requests.get(SKIN_EARN_LINK % (querys[1],0,9) )
	results2 = getSkinEarnItems(page2.text)
	print("getting skin earn items\n")
	for x in results2:
		print(x)
		
	print("sleeping for 60 seconds...\n")
	countDown(60)
	print("done")


def removeUnicode(text):
	asciiText = ''
	for char in text:
		if (ord(char) < 128):
			asciiText = asciiText + char
	return asciiText

def countDown(start_time=60):
	for x in range(start_time,0,-1):
		print(x,end='',flush=True)
		sleep(1)
		print(chr(13),end='',flush=True)
		print('      ',end='',flush=True)
		print(chr(13),end='',flush=True)
		
def breakdown(element):
	result = []
	
	name = element.find('span', {'class':"market_listing_item_name"}).encode_contents(encoding="ascii").decode('utf-8')
	quant = element.find('span',{'class': "market_listing_num_listings_qty"}).encode_contents(encoding="ascii").decode('utf-8')
	price = element.find('span', {'class':"market_table_value normal_price"}).contents[3].encode_contents(encoding="ascii").decode('utf-8')

	# print(all_divs[1].find('span', {'class':"market_listing_item_name"}).encode_contents() )
	# print(all_divs[1].find('span',{'class': "market_listing_num_listings_qty"}).encode_contents())
	# print(all_divs[1].find('span', {'class':"market_table_value normal_price"}).contents[3].encode_contents() )
	
	return item(name,quant,price)




def getSkinEarnItems(response_text):
	obj = json.loads(response_text)
	results = []
	for elm in obj['items']:
		results.append(item(elm['name'],1,elm['price']))
		
	return results
	# https://skinearn.com/api/shop?orderBy=price&order=DESC&game_id=5&name=mp5&offset=0&limit=36
	# SKIN_EARN_LINK = "https://skinearn.com/api/shop?orderBy=price&order=DESC&game_id=5&name=%s&offset=%s&limit=%s" % ('mp5',0,'9')
	
	#for elm in a['items']:
	#	print("name: %s\tid: %s\tprice: %s" % (elm['name'],elm['id'],elm['price']))
	
if __name__ == "__main__":
	launch()