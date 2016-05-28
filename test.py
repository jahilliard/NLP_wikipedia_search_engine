from lxml import html
import requests
import csv
import os.path
import pandas as pd
import numpy as np
import asyncio
import aiohttp



file_name = 'category_list/category_list.csv'
categories = []

def read_categories_to_load(file_name = 'category_list/category_list.csv'):
	categories = []
	# Read in Category List if csv exists... if not load default categories
	if os.path.isfile(file_name):
		with open(file_name, 'r') as csvfile:
			category_list = csv.reader(csvfile, delimiter=',', quotechar='|')
			for category in category_list:
				try: 
					if category[0][:3] != "###":
						categories.append(category[0].strip())
				except IndexError:
					# IndexError is okay here, because user may 
					# include extra lines in category list by mistake
					continue
	else:
		print("Custom category load file not found! Loading Default categories!")
		categories = ['Machine_learning', 'Business_software']
	return categories

async def load_page_async(session, url):
	with aiohttp.Timeout(10):
		async with session.get(url) as response:
			assert response.status == 200
			return await response.read()

def load_categories_from_wikipedia(categories = ['Machine_learning', 'Business_software']):
	temp =[]
	for category in categories:
		loop = asyncio.get_event_loop()
		connector = aiohttp.TCPConnector(verify_ssl=False)
		with aiohttp.ClientSession(loop=loop, connector=connector) as session:
			category_html = loop.run_until_complete(
				load_page_async(session, "https://en.wikipedia.org/wiki/Category:" + category))
			doc = html.fromstring(category_html)
			for page in doc.get_element_by_id("mw-pages").find_class("mw-category-group"):
				temp.append([link_data[2] for link_data in page.iterlinks()])
				# [loop.run_until_complete(load_page_async(session, link_data[2])) for link_data in page.iterlinks()]
			print(temp)

load_categories_from_wikipedia()




