import inspect
import requests
from bs4 import BeautifulSoup
from time import sleep
from item import *
import json

#NOTES:
#		timeout seems to be 60 seconds, server side
#		skinEarn limits 9, 18, 36
#		args for link 'query', offset/page, items-per-page


STEAM_URL = "https://steamcommunity.com/market/search?appid=252490&q="
QUERYS = ['unknown+territory+hoodie','mp5']
SKIN_EARN_LINK = "https://skinearn.com/api/shop?orderBy=price&order=DESC&game_id=5&name=%s&offset=%s&limit=%s"
local = False

def launch():

	
	print("getting steam items\n")
	results = getSteamItems(QUERYS[1])
	for x in results:
		print(x)
		
	
	results = getSkinEarnItems(QUERYS[1])
	print("\n\ngetting skin earn items\n")
	for x in results:
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
	
	name = element.find('span', {'class':"market_listing_item_name"}).encode_contents(encoding="ascii").decode('utf-8')
	quant = element.find('span',{'class': "market_listing_num_listings_qty"}).encode_contents(encoding="ascii").decode('utf-8')
	price = element.find('span', {'class':"market_table_value normal_price"}).contents[3].encode_contents(encoding="ascii").decode('utf-8')

	
	return item(name,quant,price)

def getSkinEarnItems(query):
	page = requests.get(SKIN_EARN_LINK % (query,0,36))
	obj = json.loads(page.text)
	results = []
	for elm in obj['items']:
		results.append(item(elm['name'],1,elm['price']))
		
	return results

def getSteamItems(query):
	
	#if local...
	#file = open('sample2.htm',encoding='utf-8')
	#soup = BeautifulSoup(file)
	
	page = requests.get(STEAM_URL + query)
	soup = BeautifulSoup(page.text,'html5lib')
	steam_rows = soup.find_all('a',{'class': "market_listing_row_link"})
	
	results = []
	for div in steam_rows:
		results.append(breakdown(div))
	return results
	
if __name__ == "__main__":
	launch()