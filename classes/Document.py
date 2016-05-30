from classes import MyPostgres as DB

class Document():

	def __init__(self, subcategory, category, full_text, full_text_no_stop, abstract, abstract_no_stop):
		self.title = subcategory.name