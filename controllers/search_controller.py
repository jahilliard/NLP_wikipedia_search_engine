from controllers import mypostgres_controller as DB

def read_terms(terms):
	term_appendage = "where term = '"
	for term in terms:
		term_appendage = term_appendage + term.lower() + "' or term = '"
	sql_to_append = str("select document_id, Sum(IDF_WEIGHT) as score from searchterm " 
					+ term_appendage[:-11] + "group by document_id order by score DESC;")
	highest_rated_docs = DB.perform_sql(sql_to_append)
	id_appendage = "where id = '"
	for id_weight in highest_rated_docs[:12]:
		id_appendage = id_appendage + str(id_weight[0]) + "' or id = '"
	sql_to_append = str("select title, doc_text from document " 
					+ id_appendage[:-9] + ";")
	highest_rated_docs = DB.perform_sql(sql_to_append)
	for doc in highest_rated_docs: 
		print(doc[0].strip() + " ")