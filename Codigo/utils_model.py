import json
import math
from nltk import FreqDist
import utils

'''Para leer los documentos'''
def read_doc(txt_path):
	with open(txt_path, "r", encoding="utf8", errors="ignore") as f:
		document = f.read()
		f.close()
		return document

'''annadimos los terminos, los creamos con un diccionario donde tengan su tf, idf, w y 
los documentos en los que estan, para que sea mas facil acceder a ellos'''
def add_terms(doc, terms, data):

	freq = FreqDist(terms)
	max_freq = max(freq.values()if len(freq)>0 else [0])

	for term in freq.keys():
		normalize_tf = freq[term] / max_freq
		new_doc = {'tf': normalize_tf,
				   'weight': 0}
		in_data = False
		for term_data in data:
			if term == term_data['key']:

				'''Actualizamos el termino'''
				term_data['value']['documents'][doc] = new_doc
				in_data = True
				break

		if not in_data:
			'''Annadimos un nuevo termino'''
			data.append({'key': term,
						 'value': {'idf':0,
									'documents': {doc:new_doc}}})


'''Calculamos el idf de cada termino y lo annadimos al diccionario'''
def add_idfs(data, N):
	for term in data:
		term['value']['idf'] = math.log10((N / len(term['value']['documents'])) + 1)


'''Calculamos el peso de cada termino por cada documento'''
def add_w(data,a):

	for term in data:
		for doc in term['value']['documents'].keys():

			term['value']['documents'][doc]['weight'] = tf_idf(data, term, (doc,term['value']['documents'][doc]),a)


'''metodo auxiliar para el peso'''
def tf_idf(data, term, document,a):
	
	term = term['value']

	w = (a + (1 - a)* document[1]['tf']) * term['idf']

	return w 

'''Guardamos el peso de cada termino por cada documento que este en la consulta '''
def documents_with_query(query_terms):

	docs = {}
	for term in query_terms:
		json_respons = json.loads(utils.start(json.dumps({'action':'get', 'key':term})))
		if json_respons['success']:
			term_value = json_respons['value']
			for doc in term_value['documents'].keys():
				if doc not in docs:
					docs[doc] = {'terms': {term: 0}, 'weights': [term_value['documents'][doc]['weight']]}
				else:
					docs[doc]['terms'][term] = len(docs[doc]['weights'])
					docs[doc]['weights'].append(term_value['documents'][doc]['weight'])

	return docs

def dj():
	docs = {}
	json_respons = json.loads(utils.start(json.dumps({'action':'dict'})))
	for item in json_respons.keys():
		result = json_respons[item]
		for document in result['documents']:
			if document not in docs:
				docs[document] = {'w': (result['documents'][document]['weight'])**2}
			else:
				docs[document]['w'] += (result['documents'][document]['weight'])**2

	for item in docs:
		docs[item]['w'] = math.sqrt(docs[item]['w'])

	return docs

def q(query_data):
	query_w = {}
	for item in query_data:
		if 'query' not in query_w:
			query_w['query'] = (item['value']['documents']['query']['weight'])**2
		else:
			query_w['query'] += (item['value']['documents']['query']['weight'])**2
	query_w['query'] = math.sqrt(query_w['query'])
	return query_w

def djq(query_data, docs):
	dicc_ranking = {}
	for doc in docs.keys():
		for tm_query in query_data:
			if tm_query['key'] in docs[doc]['terms'].keys():

				weight_query = tm_query['value']['documents']['query']['weight']
				index_weight_data = docs[doc]['terms'][tm_query['key']]
				weight_data = docs[doc]['weights'][index_weight_data]
				if doc not in dicc_ranking:
					dicc_ranking[doc] = (weight_query * weight_data)
				else:
					dicc_ranking[doc] += weight_query * weight_data
					
	return dicc_ranking

'''Calculamos el ranking de los documentos con la funcion de ranking
del modelo vectorial'''
def sim(query_data, query_terms):
	'''Vemos los documentos que contengan algun termino de la consulta'''
	docs = documents_with_query(query_terms)
	docs_w = dj()
	q_w = q(query_data)
	djq_w = djq(query_data, docs)
	dicc_ranking = {}
	for doc in docs.keys():
		if doc not in dicc_ranking:
			dicc_ranking[doc] = (djq_w[doc]/(docs_w[doc]['w']*q_w['query']))
	return dicc_ranking
					
	
