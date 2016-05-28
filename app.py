from lxml import html
import requests
import csv
import os.path
import pandas as pd
import numpy as np

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

def load_categories_from_wikipedia(categories = ['Machine_learning', 'Business_software', 'Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software', 'Machine_learning', 'Business_software', 'Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software','Machine_learning', 'Business_software']):
	temp =[]
	for category in categories:
		page = requests.get("https://en.wikipedia.org/wiki/Category:" + category).text
		# doc = html.fromstring(page)
		# for page in doc.get_element_by_id("mw-pages").find_class("mw-category-group"):
		# 	temp.append([n[2] for n in page.iterlinks()])
	print("done")


load_categories_from_wikipedia()





