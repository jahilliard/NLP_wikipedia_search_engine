import sys
from controllers import mypostgres_controller as db

def main_router(args):
	if args[1] == "/install":
		print("install")
		db.build_db()
		db.close_connection()

	# TESTS: really basic tests For Dev purposes 
	elif args[1] == "/tests":
		try:
			db.build_db()
			print('\033[92m' + "	PASS:\033[94m DB Build pass\033[0m")
		except:
			print('\033[91m' + "	FAIL: DB Build fail\033[0m")
		try:
			db.drop_tables()
			print('\033[92m' + "	PASS:\033[94m Drop DB tables pass\033[0m")
		except:
			print('\033[91m' + "	FAIL: DB Build fail\033[0m") 
		try:
			db.close_connection()
			print('\033[92m' + "	PASS:\033[94m Close DB connection pass\033[0m")
		except:
			print('\033[91m' + "	FAIL: Close DB connection fail\033[0m") 
		
main_router(sys.argv)

