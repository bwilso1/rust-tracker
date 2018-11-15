import inspect
import requests
from bs4 import BeautifulSoup
from time import sleep

#NOTES:
#		timeout seems to be 60 seconds, server side


URL = "https://steamcommunity.com/market/search?appid=252490&q="
querys = ['unknown+territory+hoodie','mp5']

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
	result = []
	
	result.append(element.find('span', {'class':"market_listing_item_name"}).encode_contents(encoding="ascii").decode('utf-8') )
	result.append(element.find('span',{'class': "market_listing_num_listings_qty"}).encode_contents(encoding="ascii").decode('utf-8') )
	result.append(element.find('span', {'class':"market_table_value normal_price"}).contents[3].encode_contents(encoding="ascii").decode('utf-8') )

	# print(all_divs[1].find('span', {'class':"market_listing_item_name"}).encode_contents() )
	# print(all_divs[1].find('span',{'class': "market_listing_num_listings_qty"}).encode_contents())
	# print(all_divs[1].find('span', {'class':"market_table_value normal_price"}).contents[3].encode_contents() )
	
	return result
	
if __name__ == "__main__":
	launch()