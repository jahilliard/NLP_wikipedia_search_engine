from classes import MyPostgres as DB

class Document():

	def __init__(self, subcategory, full_text):
		self.title = subcategory.name
		self.subcategory = subcategory
		self.full_text = full_text