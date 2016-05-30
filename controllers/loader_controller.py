# Probably should break this controller up, but time constrainsts...

from lxml import html
import csv
import os.path
import asyncio
import aiohttp
import urllib
from classes import Category as cat
from classes import Subcategory as subcat 
from classes import Document as doc

# Would need to refactor style to change this global... OK for current purposes
subpage_categories = []

def read_categories_to_load(file_name = 'category_list/category_list.csv'):
	categories = []
	# Read in Category List if csv exists... if not load default categories
	if os.path.isfile(file_name):
		with open(file_name, 'r') as csvfile:
			category_list = csv.reader(csvfile, delimiter=',', quotechar='|')
			for category in category_list:
				try: 
					if category[0][:3] != "###":
						categories.append(cat.Category(name = category[0].strip().replace("_", " "), 
							url = "https://en.wikipedia.org/wiki/Category:" + category[0].strip()))
				except IndexError:
					# IndexError is okay here, because user may 
					# include extra lines in category list by mistake
					continue
	else:
		print("Custom category load file not found! Loading Default categories!")
		categories = [cat.Category(name= 'Machine_learning'.replace ("_", " ") , 
						url = "https://en.wikipedia.org/wiki/Category:Machine_learning"), 
						cat.Category(name= 'Business_software'.replace ("_", " ") , 
						url = "https://en.wikipedia.org/wiki/Category:Business_software")]
	return categories


@asyncio.coroutine
def load_page_async(url, category = None, is_subpage = False):
	connector = aiohttp.TCPConnector(verify_ssl=False)
	with aiohttp.ClientSession(connector=connector) as session:
		with aiohttp.Timeout(10):
			response = yield from session.get(urllib.parse.unquote(url))
			assert response.status == 200
			content = yield from response.read()
	if is_subpage == False:
		manipulate_content(content, category)
	else:
		print(content)
	return 

def manipulate_content(content, category = None, is_subpage = False):
	doc = html.fromstring(content)
	if is_subpage == False:
		for page in doc.get_element_by_id("mw-pages").find_class("mw-category-group"):
			subpage_categories.append([subcat.Subcategory(url = "https://en.wikipedia.org" + link_data[2],
 														name =  link_data[2][6:].replace("_", " "),
 														category = category)
										for link_data in page.iterlinks()])

# ['Machine_learning', 'Business_software', 'Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software', 'Machine_learning', 'Business_software', 'Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software']
def load_categories_from_wikipedia(categories):
	# async lib runs O(log(n))... requests is O(n)
	# TODO: figure out how to load to async queue
	async_tasks = []
	loop = asyncio.get_event_loop()
	for category in categories:
		action_item = load_page_async(category.url, category)
		async_tasks.append(action_item)
	loop.run_until_complete(asyncio.wait(async_tasks))
	loop.close()
	return subpage_categories


