import requests
import json

class StockX():

	def __init__(self):
		self.getPrices()

	def getPrices(self):
		NotreArray = self.loadSKUS()
		headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"}
		base_url_beginning = 'https://stockx.com/api/browse?productCategory=sneakers&_search='
		base_url_ending = '&dataType=product'
		
		data = []
		for SKU,NotrePrice in NotreArray:
			url = base_url_beginning + SKU + base_url_ending
			response = requests.get(url, headers=headers).json()
			products = response['Products']

			brands = []
			highestBids = []
			lowestAsks = []
			for product in products:
				brand = product['brand']
				market = product['market']
				highestBid = market['highestBid']
				lowestAsk = market['lowestAsk']

				brands.append(brand)
				highestBids.append(highestBid)
				lowestAsks.append(lowestAsk)

			data.append({
				"SKU": SKU, 
				"NotrePrice": NotrePrice, 
				"brands": brands, 
				"highestBids" : highestBids, 
				"lowestAsks" : lowestAsks
				})

		with open('stockX.json', 'w') as outfile:
			json.dump(data, outfile, indent=4)
            	

	def loadSKUS(self):
		with open('../../NOTRE_SKUS.json') as json_file:
			data = json.load(json_file)
			NotreArray = []
			for i in data:
				NotreArray.append({i['SKU'],i['NotrePrice']})
			return NotreArray

StockX()
