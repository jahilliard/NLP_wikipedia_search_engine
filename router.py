import sys
from controllers import mypostgres_controller as DB
from controllers import loader_controller as Loader
from controllers import model_trainer_controller as model_trainer
from controllers import search_controller as search

def download(filename):
	categories = Loader.read_categories_to_load(filename)
	subcat = Loader.load_categories_from_wikipedia(categories)
	subcat = [item for sublist in subcat for item in sublist]
	docs = Loader.load_categories_from_wikipedia(subcat, is_subpage = True)
	model_trainer.calculate_tfidf_all_docs(docs)
	return



def main_router(args):
	if args[1] == "/install":
		if len(args) > 2:
			filename = args[2]
		else:
			filename = 'category_list/category_list.csv'
		print("install")
		DB.build_db()
		download(filename)
		DB.close_connection()

	elif args[1] == "/download":
		if len(args) > 2:
			filename = args[2]
		else:
			filename = 'category_list/category_list.csv'
		download_test(filename)

	# TESTS: really basic tests For Dev purposes 
	elif args[1] == "/all_tests":
		if len(args) > 2:
			filename = args[2]
		else:
			filename = 'category_list/category_list.csv'
		build_test() 
		download_test(filename)
		drop_test()
		close_test()

	elif args[1] == "/search": 
		search_terms = []
		if len(args) > 2:
			for search_term in args[2:]:
				search_terms.append(search_term)
			search.read_terms(search_terms)
		else:
			return

		

	elif args[1] == "/build":
		build_test()
		close_test()

	elif args[1] == "/download":
		if len(args) > 2:
			filename = args[2]
		else:
			filename = 'category_list/category_list.csv'
		download_test(filename)
		close_test()

	elif args[1] == "/drop":
		drop_test()
		close_test()

def drop_test():
	try:
		DB.drop_tables()
		print('\033[92m' + "	PASS:\033[94m Drop DB tables pass\033[0m")
	except:
		print('\033[91m' + "	FAIL: DB Build fail\033[0m") 

def close_test():
	try:
		DB.close_connection()
		print('\033[92m' + "	PASS:\033[94m Close DB connection pass\033[0m")
	except:
		print('\033[91m' + "	FAIL: Close DB connection fail\033[0m") 

def build_test():
	try:
		DB.build_db()
		print('\033[92m' + "	PASS:\033[94m DB Build pass\033[0m")
	except:
		print('\033[91m' + "	FAIL: DB Build fail\033[0m")

def download_test(filename):
	try:
		download(filename)
		print('\033[92m' + "	PASS:\033[94m Download Step pass\033[0m")
	except:
		print('\033[91m' + "	FAIL: Download Step fail\033[0m") 

main_router(sys.argv)

