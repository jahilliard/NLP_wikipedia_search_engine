# To Learn about lib reference http://www.tutorialspoint.com/postgresql/postgresql_python.htm
import psycopg2

class MyPostgres:

	def __init__(self):
		try:
			self.conn = psycopg2.connect(database="wikisearch", host="127.0.0.1", port="5432")
		except:
			print("Cannot Connect to DB")

	def buid_db:
		try:
			cur = self.conn.cursor()
			cur.execute('''CREATE TABLE CATEGORY
				(ID INT SERIAL PRIMARY KEY     NOT NULL,
					NAME           CHAR(250)    NOT NULL,
					URL            CHAR(250)     NOT NULL);''')
			cur.execute('''CREATE TABLE SUBCATEGORY
				(ID INT SERIAL PRIMARY KEY     NOT NULL,
					CATEGORY_ID    INT      references CATEGORY(ID) NOT NULL,
					NAME           CHAR(250)    NOT NULL,
					URL            CHAR(250)     NOT NULL);''')
			cur.execute('''CREATE TABLE DOCUMENT
				(ID INT SERIAL PRIMARY KEY     NOT NULL,
					CATEGORY_ID    	  INT      references CATEGORY(ID) NOT NULL,
					SUBCATEGORY_ID    INT      references SUBCATEGORY(ID) NOT NULL,
					TITLE             CHAR(250)    NOT NULL,
					DOC_TEXT          TEXT     NOT NULL,
					DOC_TEXT_NO_STOP  TEXT     NOT NULL);''')
			cur.execute('''CREATE TABLE SEARCHTERM
				(ID INT SERIAL PRIMARY KEY     NOT NULL,
					TERM           CHAR(500)    NOT NULL);''')
			cur.execute('''CREATE TABLE CATEGORYTERM
				(ID INT SERIAL PRIMARY KEY     NOT NULL,
					DOCUMENT_ID    	  INT      references DOCUMENT(ID) NOT NULL,
					SEARCH_TERM_ID    INT      references SEARCHTERM(ID) NOT NULL,
					IDF_WEIGHT        REAL     NOT NULL,);''')
		except:
			print("Cannot build DB");
	
	# table: table to insert into
	# insert_items: list of dicts to insert... 
	# ie namedict = [{"first_name":"Joshua", "last_name":"Drake"},
	#                {"first_name":"Steven", "last_name":"Foo"},
	#                {"first_name":"David", "last_name":"Bar"}]
	def preform_insert(statement, table, insert_items):
		col_string = "("
		val_string = "("
		for key in insert_items:
			val_string += "%(" + key + ")s, "
			col_string += key + ", "
		val_string = val_string[:-2] + ")"
		col_string = col_string[:-2] + ")"
		try:
			cur = self.conn.cursor()

			cur.executemany("INSERT INTO " + table + col_string + " VALUES " + val_string + ";"
				, insert_items)
		except:
			print("Cannot Insert items \n" + statement + "\n" + insert_items)

	# statement: SQL statement to preform
	def preform_select(statement):
		try:
			# turns what we return into a dictionary... ie print ("   ", row['notes'][1])
			cur = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
			cur.execute(statement)
			rows = cur.fetchall()
			return rows
		except:
			print("Cannot Preform Select Statement " + statement)

	def close_connection:
		self.conn.commit()
		self.conn.close()
