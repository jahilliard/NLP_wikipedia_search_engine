from classes import MyPostgres

# not sure when to close this 
myconnection = MyPostgres.MyPostgres()

def build_db():
	myconnection.buid_db()

def perform_insert(table, items):
	col_string = "("
	val_string = "("
	for key, val in items[0].items():
		val_string =  val_string + "%(" + key + ")s, "
		col_string = col_string + key + ", "
	val_string = val_string[:-2] + ")"
	col_string = col_string[:-2] + ")"
	myconnection.perform_insert(table = table, insert_items = items, 
								val_string = val_string, col_string = col_string)

def perform_sql(statement):
	return myconnection.preform_sql_fetch(statement = statement)

def drop_tables():
	myconnection.drop_tables()

def close_connection():
	myconnection.close_connection()

