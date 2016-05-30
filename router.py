import sys
from controllers import mypostgres_controller as DB
from controllers import loader_controller as Loader

def download(filename):
	categories = Loader.read_categories_to_load(filename)
	print(categories)
	subcat = Loader.load_categories_from_wikipedia(categories)
	print(subcat)

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
	elif args[1] == "/tests":
		try:
			DB.build_db()
			print('\033[92m' + "	PASS:\033[94m DB Build pass\033[0m")
		except:
			print('\033[91m' + "	FAIL: DB Build fail\033[0m")
		try:
			download(filename)
			print('\033[92m' + "	PASS:\033[94m Download Step pass\033[0m")
		except:
			print('\033[91m' + "	FAIL: Download Step fail\033[0m") 
		try:
			DB.drop_tables()
			print('\033[92m' + "	PASS:\033[94m Drop DB tables pass\033[0m")
		except:
			print('\033[91m' + "	FAIL: DB Build fail\033[0m") 
		try:
			DB.close_connection()
			print('\033[92m' + "	PASS:\033[94m Close DB connection pass\033[0m")
		except:
			print('\033[91m' + "	FAIL: Close DB connection fail\033[0m") 
		
main_router(sys.argv)

