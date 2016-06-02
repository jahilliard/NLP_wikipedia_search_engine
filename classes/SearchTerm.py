import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from controllers import mypostgres_controller as DB

class SearchTerm():

	def __init__(self, word, tfidf, document):
		self.term = word
		self.tfidf = tfidf
		self.document = document
		self.check_if_exist()

	def store_category(self):
		DB.perform_insert(table = "SEARCHTERM", items = [{"term": self.term,
														"DOCUMENT_ID": self.document.id,
														"IDF_WEIGHT": self.tfidf}])

	def get_id(self):
		return DB.perform_sql(str("Select ID from SEARCHTERM where DOCUMENT_ID = " 
										+ str(self.document.id) + " AND term = '"
											+ str(self.term) + "';"))[0][0]

	def check_if_exist(self):
		does_exist = DB.perform_sql(str("Select ID from SEARCHTERM where DOCUMENT_ID = " 
										+ str(self.document.id) + " AND term = '"
											+ str(self.term) + "';"))
		if len(does_exist) > 0:
			self.id = does_exist[0][0]
		else:
			self.store_category()
			self.id = self.get_id()

