import sys
from controllers import mypostgres_controller as db

def main_router(args):
	if args[1] == "/install":
		print("install")
		db.build_db()
		db.close_connection()

	# For Dev purposes 
	elif args[1] == "/drop_tabs":
		print("drop_tabs")
		db.drop_tables()
		db.close_connection()
		
main_router(sys.argv)

