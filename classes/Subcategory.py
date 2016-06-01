import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from controllers import mypostgres_controller as DB

class Subcategory():

	def __init__(self, url, name, category):
		self.url = url
		self.name = name
		self.category = category
		self.__check_if_exist(name = self.name)


	def store_category(self):
		DB.perform_insert(table = "Subcategory", items = [{"name": self.name,
														"url": self.url,
														"category_id": self.category.id}])

	def get_id(self):
		return DB.perform_sql("Select ID from Subcategory where name = '" 
			+ self.name +"';")[0][0]

	def __check_if_exist(self, name):
		does_exist = DB.perform_sql("Select ID from Subcategory where name = '"+ name +"';")
		if len(does_exist) > 0:
			self.id = does_exist[0][0]
		else:
			self.store_category()
			self.id = self.get_id()



