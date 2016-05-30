import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from controllers import mypostgres_controller as DB

class Category():

	def __init__(self, name, url):
		self.url = url 
		self.name = name
		self.store_category()
		self.id = self.get_id()

	def store_category(self):
		DB.perform_insert(table = "Category", items = [{"name": self.name,
														"url": self.url}])

	def get_id(self):
		return DB.perform_sql("Select ID from Category where name = '" + self.name +"';")[0][0]