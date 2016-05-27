from lxml import html
import requests
import csv
import os.path

file_name = '/category_list/category_list.csv'
categories = []

# Read in Category List if csv exists... if not load default categories
if os.path.isfile(file_name):
	with open(file_name, 'rb') as csvfile:
		category_list = csv.reader(csvfile, delimiter=', ', quotechar='|')
		for category in category_list:
			print(category)
else:
	print("file not found!")