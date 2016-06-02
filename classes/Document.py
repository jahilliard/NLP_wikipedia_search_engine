import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from controllers import mypostgres_controller as DB
from nltk.corpus import stopwords
import string

# reiniting this var everytime is slow
cachedStopWords = stopwords.words("english")
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)

class Document():

	def __init__(self, subcategory, full_text):
		self.title = subcategory.name
		self.subcategory = subcategory
		self.full_text = full_text
		self.check_if_exist()

	def store_category(self):
		self.full_text_no_stop = " ".join([i for i in self.full_text.split() if i not in cachedStopWords])
		self.full_text_no_stop = self.full_text_no_stop.translate(remove_punctuation_map)
		self.full_text_no_stop = self.full_text_no_stop.lower()
		DB.perform_insert(table = "DOCUMENT", items = [{"title": self.title,
														"DOC_TEXT": self.full_text,
														"DOC_TEXT_NO_STOP": self.full_text_no_stop,
														"CATEGORY_ID": self.subcategory.category.id,
														"SUBCATEGORY_ID": self.subcategory.id}])

	def get_id(self):
		return DB.perform_sql(str("Select ID from document where category_id = "+ 
									str(self.subcategory.category.id) + " and subcategory_id = " 
									+ str(self.subcategory.id) + ";"))[0][0]

	def check_if_exist(self):
		does_exist = DB.perform_sql(str("Select ID from document where category_id = "+ 
									str(self.subcategory.category.id) + " and subcategory_id = " 
									+ str(self.subcategory.id) + ";"))
		if len(does_exist) > 0:
			self.id = does_exist[0][0]
		else:
			self.store_category()
			self.id = self.get_id()



