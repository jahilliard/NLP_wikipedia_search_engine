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

@asyncio.coroutine
def load_page_async(url):
	connector = aiohttp.TCPConnector(verify_ssl=False)
	with aiohttp.ClientSession(connector=connector) as session:
		with aiohttp.Timeout(10):
			response = yield from session.get(url)
			assert response.status == 200
			content = yield from response.read()
		# async with session.get(url) as response:
		# 	assert response.status == 200
		# 	return await response.read()

# ['Machine_learning', 'Business_software', 'Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software', 'Machine_learning', 'Business_software', 'Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software']
def load_categories_from_wikipedia(categories = ['Machine_learning', 'Business_software', 'Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software', 'Machine_learning', 'Business_software', 'Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software']):
	async_tasks = []
	loop = asyncio.get_event_loop()
	for category in categories:
		action_item = load_page_async("https://en.wikipedia.org/wiki/Category:" + category)
		async_tasks.append(action_item)
	loop.run_until_complete(asyncio.wait(async_tasks))
	loop.close()



	# 		doc = html.fromstring(category_html)
	# 		for page in doc.get_element_by_id("mw-pages").find_class("mw-category-group"):
	# 			temp.append([link_data[2] for link_data in page.iterlinks()])
	# 			# [loop.run_until_complete(load_page_async(session, link_data[2])) for link_data in page.iterlinks()]
	# print("done")


# ['Machine_learning', 'Business_software', 'Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software', 'Machine_learning', 'Business_software', 'Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software']
# def load_categories_from_wikipedia(categories = ['Machine_learning', 'Business_software']):
# 	async_load_list =[]
# 	for category in categories:
# 		# see a 22% speed increase using grequests lib over requests and aiohttp
# 		async_action_item = grequests.get("https://en.wikipedia.org/wiki/Category:" + category, 
# 			hooks = {"response": load_page})
# 		async_load_list.append(async_action_item)
# 	grequests.map(async_load_list)


# def load_page(response):
# 	print(response.text)
# 	# doc = html.fromstring(response)
# 	# for page in doc.get_element_by_id("mw-pages").find_class("mw-category-group"):
# 	# temp.append([n[2] for n in page.iterlinks()])
# 	print("done")

load_categories_from_wikipedia()

# import asyncio
 

# def do_work(task_name, work_queue):
#     while not work_queue.empty():
#         queue_item = yield from work_queue.get()
#         print('{0} grabbed item: {1}'.format(task_name, queue_item))
#         yield from asyncio.sleep(0.5)
 
 
# if __name__ == "__main__":
#     q = asyncio.Queue()
 
#     for x in range(20):
#         q.put_nowait(x)
 
#     print(q)
 
#     loop = asyncio.get_event_loop()
 
#     tasks = [
#         asyncio.async(do_work('task1', q)),
#         asyncio.async(do_work('task2', q)),
#         asyncio.async(do_work('task3', q))]
 
#     loop.run_until_complete(asyncio.wait(tasks))
#     loop.close()

#     import asyncio
# import aiohttp
 
# @asyncio.coroutine
# def fetch_page(url, pause=False):
#     if pause:
#         yield from asyncio.sleep(2)
 
#     response = yield from aiohttp.request('GET', url)
#     assert response.status == 200
#     content = yield from response.read()
#     print('URL: {0}:  Content: {1}'.format(url, content))
 
 
# loop = asyncio.get_event_loop()
# tasks = [
#     fetch_page('http://google.com'),
#     fetch_page('http://cnn.com', True),
#     fetch_page('http://twitter.com')]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()
 
# for task in tasks:
#     print(task)




