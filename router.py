import sys
from controllers import mypostgres_controller as DB
from controllers import loader_controller as Loader

def download(filename):
	categories = Loader.read_categories_to_load(filename)
	subcat = Loader.load_categories_from_wikipedia(categories)
	subcat = [item for sublist in subcat for item in sublist]
	docs = Loader.load_categories_from_wikipedia(subcat, is_subpage = True)
	return

def main_router(args):
	if len(args) > 2:
		filename = args[2]
	else:
		filename = 'category_list/category_list.csv'

	if args[1] == "/install":
		print("install")
		DB.build_db()
		DB.close_connection()

	elif args[1] == "/download":
		download(filename)

	# TESTS: really basic tests For Dev purposes 
	elif args[1] == "/all_tests":
		build_test() 
		download_test()
		drop_test()
		close_test()

	elif args[1] == "/build":
		build_test()
		close_test()

	elif args[1] == "/download":
		download_test()
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

def download_test():
	try:
		download(filename)
		
		print('\033[92m' + "	PASS:\033[94m Download Step pass\033[0m")
	except:
		print('\033[91m' + "	FAIL: Download Step fail\033[0m") 

main_router(sys.argv)

