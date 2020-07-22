import inspect
import requests
from bs4 import BeautifulSoup
from time import sleep
from item import *
import json
from manager import DataFileManager,Holder

#NOTES:
#		timeout seems to be 60 seconds, server side
#		skinEarn limits 9, 18, 36
#		args for link 'query', offset/page, items-per-page


STEAM_BASE_URL = "https://steamcommunity.com/market/search?appid=252490&q="

SKIN_EARN_LINK = "https://skinearn.com/api/shop?orderBy=price&order=DESC&game_id=5&name=%s&offset=%s&limit=%s"

STEAM_URLS = {'armor' : 'https://steamcommunity.com/market/search?category_252490_itemclass%5B%5D=any&category_252490_steamcat%5B%5D=tag_steamcat.armor&appid=252490&q=',
		    'weapon' : 'https://steamcommunity.com/market/search?category_252490_itemclass%5B%5D=any&category_252490_steamcat%5B%5D=tag_steamcat.weapon&appid=252490&q=',
		    'clothing' : 'https://steamcommunity.com/market/search?category_252490_itemclass%5B%5D=any&category_252490_steamcat%5B%5D=tag_steamcat.clothing&appid=252490&q='}

STEAM_QUERIES = [['armor','carbon-metalhunter-army-stainless+NOT+armored+NOT+Plate'],
			  ['armor','plate-press+NOT+engineer+NOT+conquistador+NOT+machina+NOT+looter+NOT+racing+NOT+hazard+NOT+wander+NOT+Space'],
			  ['weapon','mp5-pearl+NOT+wild+NOT+dead+NOT+wasp+NOT+spitfire+NOT+nomad']
			  ]
WAIT_TIME = 65

SKIN_EARN_QUERIES = ['mp5', 'pearl+python','face','metalhunter','christmas+lights','press']

OUTFILE = 'stats.json'
def launch():

	one_run_holder = Holder()
	for tmp in STEAM_QUERIES:
		query = STEAM_URLS[tmp[0]] + tmp[1]
		print("steam query: %s" % (query,))
		results = getSteamItems(query)
		for item in results:
			one_run_holder.addDollars(item.name, item.price)
		
		countDown(WAIT_TIME)
	
	for tmp in SKIN_EARN_QUERIES:
		query = SKIN_EARN_LINK % (tmp,0,36)
		print("skin earn query: %s" % (query,))
		results = getSkinEarnItems(query)
		for item in results:
			one_run_holder.addCoins(item.name,item.price)
		countDown(15)
		
	tmp = one_run_holder.dumpDict()
	keys = tmp.keys()
	manager = DataFileManager(OUTFILE)
	for key in keys:
		manager.add(key,tmp[key]['dollars'],tmp[key]['coins'])
		
	manager.dump(OUTFILE)
		
	
	
	


def removeUnicode(text):
	asciiText = ''
	for char in text:
		if (ord(char) < 128):
			asciiText = asciiText + char
	return asciiText

def countDown(start_time=60):
	print("sleeping for %s seconds" % start_time)
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
	page = requests.get(query)
	obj = json.loads(page.text)
	results = []
	for elm in obj['items']:
		results.append(item(elm['name'],1,elm['price']))
		
	return results

def getSteamItems(query):
	
	#if local...
	#file = open('sample2.htm',encoding='utf-8')
	#soup = BeautifulSoup(file)
	
	page = requests.get(query)
	soup = BeautifulSoup(page.text,'html5lib')
	steam_rows = soup.find_all('a',{'class': "market_listing_row_link"})
	
	results = []
	for div in steam_rows:
		results.append(breakdown(div))
	return results

	#plate-press+NOT+engineer+NOT+conquistador+NOT+machina+NOT+looter+NOT+racing+NOT+hazard+NOT+wander+NOT+Space
	
	#weapons
	#mp5-pearl+NOT+wild+NOT+dead+NOT+wasp+NOT+spitfire+NOT+nomad
	
	
if __name__ == "__main__":
	launch()