# To Learn about lib reference http://www.tutorialspoint.com/postgresql/postgresql_python.htm
import psycopg2

class MyPostgres:

	def __init__(self):
		try:
			self.conn = psycopg2.connect(database="wikisearch", host="127.0.0.1", port="5432")
		except:
			print("Cannot Connect to DB")

	# builds database tables
	# TODO: check to see if tables exist... eventually want to 
	# 		build up db not just destroy everytime... LOL!!
	def buid_db(self):
		try:
			cur = self.conn.cursor()
			cur.execute('''CREATE TABLE CATEGORY
				(ID SERIAL PRIMARY KEY     NOT NULL,
					NAME           CHAR(250)    NOT NULL,
					URL            CHAR(250)     NOT NULL);''')
			cur.execute('''CREATE TABLE SUBCATEGORY
				(ID SERIAL PRIMARY KEY     NOT NULL,
					CATEGORY_ID    INT      references CATEGORY(ID) NOT NULL,
					NAME           CHAR(250)    NOT NULL,
					URL            CHAR(250)     NOT NULL);''')
			cur.execute('''CREATE TABLE DOCUMENT
				(ID SERIAL PRIMARY KEY     NOT NULL,
					CATEGORY_ID    	  INT      references CATEGORY(ID) NOT NULL,
					SUBCATEGORY_ID    INT      references SUBCATEGORY(ID) NOT NULL,
					TITLE             CHAR(250)    NOT NULL,
					DOC_TEXT          TEXT     NOT NULL,
					DOC_TEXT_NO_STOP  TEXT     NOT NULL);''')
			cur.execute('''CREATE TABLE SEARCHTERM
				(ID SERIAL PRIMARY KEY     NOT NULL,
					TERM           CHAR(500)    NOT NULL);''')
			cur.execute('''CREATE TABLE CATEGORYTERM
				(ID SERIAL PRIMARY KEY     NOT NULL,
					DOCUMENT_ID    	  INT      references DOCUMENT(ID) NOT NULL,
					SEARCH_TERM_ID    INT      references SEARCHTERM(ID) NOT NULL,
					IDF_WEIGHT        REAL     NOT NULL);''')
			cur.close()
			self.conn.commit()
		except:
			print("Cannot build DB");
	
	# table: table to insert into
	# insert_items: list of dicts to insert... 
	# ie namedict = [{"first_name":"Joshua", "last_name":"Drake"},
	#                {"first_name":"Steven", "last_name":"Foo"},
	#                {"first_name":"David", "last_name":"Bar"}]
	def perform_insert(self, table, insert_items, col_string, val_string):
		try:
			cur = self.conn.cursor()

			cur.executemany("INSERT INTO " + table + col_string + " VALUES " + val_string + ";"
				, insert_items)
			cur.close()
			self.conn.commit()
		except:
			print("Cannot Insert items \n" + table + "\n" + insert_items)

	# statement: SQL statement to preform
	def preform_sql_fetch(self, statement):
		try:
			cur = self.conn.cursor()
			cur.execute(statement)
			self.conn.commit()
			rows = cur.fetchall()
			cur.close()
			return rows
		except:
			print("Cannot Preform Select Statement " + statement)

	def drop_tables(self):
		try:
			cur = self.conn.cursor()
			cur.execute('''DROP TABLE CATEGORYTERM CASCADE;''')
			cur.execute('''DROP TABLE SEARCHTERM CASCADE;''')
			cur.execute('''DROP TABLE DOCUMENT CASCADE;''')
			cur.execute('''DROP TABLE SUBCATEGORY CASCADE;''')
			cur.execute('''DROP TABLE CATEGORY CASCADE;''')
			cur.close()
			self.conn.commit()
		except:
			print("Cannot DROP tables from DB")

	def close_connection(self):
		self.conn.close()
