from classes import MyPostgres as DB

class Category():

	def __init__(self, name, url):
		self.url = url 
		self.name = name