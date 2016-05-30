from classes import MyPostgres
	
myconnection = MyPostgres.MyPostgres()

def build_db():
	myconnection.buid_db()

def drop_tables():
	myconnection.drop_tables()

def close_connection():
	myconnection.close_connection()

