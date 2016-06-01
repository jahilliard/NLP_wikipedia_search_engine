import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from controllers import mypostgres_controller as DB

class Category():

	def __init__(self, name, url):
		self.url = url 
		self.name = name
		self.__check_if_exist(name = self.name)

	def store_category(self):
		DB.perform_insert(table = "Category", items = [{"name": self.name,
														"url": self.url}])

	def get_id(self):
		return DB.perform_sql("Select ID from Category where name = '" + self.name +"';")[0][0]

	def __check_if_exist(self, name):
		does_exist = DB.perform_sql("Select ID from Category where name = '" + name +"';")
		if len(does_exist) > 0:
			self.id = does_exist[0][0]
		else:
			self.store_category()
			self.id = self.get_id()

	def was_subcategory_queried(self):
		does_exist = DB.perform_sql(str("Select ID from subcategory where Category_id = '"
										+ str(self.id) +"' limit 1;"))
		if len(does_exist) > 0:
			return True
		else:
			return False