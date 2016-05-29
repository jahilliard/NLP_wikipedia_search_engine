from lxml import html
import csv
import os.path
import pandas as pd
import numpy as np
import asyncio
import aiohttp

file_name = 'category_list/category_list.csv'

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


@asyncio.coroutine
def load_page_async(url, is_subpage = False):
	connector = aiohttp.TCPConnector(verify_ssl=False)
	with aiohttp.ClientSession(connector=connector) as session:
		with aiohttp.Timeout(10):
			response = yield from session.get(url)
			assert response.status == 200
			content = yield from response.read()
	if is_subpage == False:
		manipulate_content(content)
	else:
		print(content)
	return 

def manipulate_content(content):
	doc = html.fromstring(content)
	print("Hit content manipulate_content")
	for page in doc.get_element_by_id("mw-pages").find_class("mw-category-group"):
		subpage_categories.append([link_data[2] for link_data in page.iterlinks()])
	# subpage_categories.append([item for sublist in subpage_categories_temp for item in sublist])



# ['Machine_learning', 'Business_software', 'Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software', 'Machine_learning', 'Business_software', 'Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software']
def load_categories_from_wikipedia(categories = ['Machine_learning', 'Business_software']):
	# async lib runs O(log(n))... requests is O(n)
	# TODO: figure out how to load to async queue
	async_tasks = []
	loop = asyncio.get_event_loop()
	for category in categories:
		action_item = load_page_async("https://en.wikipedia.org/wiki/Category:" + category)
		async_tasks.append(action_item)
	loop.run_until_complete(asyncio.wait(async_tasks))
	loop.close()
	print(subpage_categories)

categories = read_categories_to_load(file_name = 'category_list/category_list.csv')
subpage_categories = []

load_categories_from_wikipedia()


