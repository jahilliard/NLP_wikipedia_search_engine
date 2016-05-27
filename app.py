from lxml import html
import requests
import csv
import os.path

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
					continue
					# IndexError is okay here, because user may 
					# include extra lines in category list by mistake
	else:
		print("Custom category load file not found! Loading Default categories!")
		categories = ['Machine_learning', 'Business_software']
	return categories


print(read_categories_to_load())