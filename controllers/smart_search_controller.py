import math
from textblob import TextBlob as tb

pre_mapped_words = dict()

def tf(word, blob):
	return blob.words.count(word) / len(blob.words)

def n_containing(word, bloblist):
	if word in pre_mapped_words:
		return pre_mapped_words[word]
	else:
		pre_mapped_words[word] = sum(1 for blob in bloblist if word in blob.words)
		return pre_mapped_words[word]

def idf(word, bloblist):
	return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))

def tfidf(word, blob, bloblist):
	return tf(word, blob) * idf(word, bloblist)

def calculate_tfidf_all_docs(list_of_docs):
	bloblist = [tb(doc.full_text_no_stop) for doc in list_of_docs]
	for blob in bloblist:
		for word in blob.words:
			
