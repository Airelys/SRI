import os
import glob
import sys
import json
import utils
from text_processing import text_processing
from utils_model import read_doc
from utils_model import add_terms
from utils_model import add_idfs
from utils_model import add_w
from utils_model import documents_with_query
from utils_model import sim


def model(json_request):

	data = json.loads(json_request)

	'''si vamos a procesar los documentos'''
	if data['action'] == 'build':
		documents(data['path'])

	#Si vamos a procesar la consulta
	elif data['action'] == 'query':
		return query(data['query'], data['count'])



def documents(path):

	data = []

	'''Buscamos en que sistema operativo estamos para ver si tenemos q usar para el path \ o /'''
	if 'win' in sys.platform:
		_path = path + "\**"
	else:
		_path = path + "/**"
    
	'''Verificamos que el path existe'''
	if os.path.exists(path):
		all_docs_txt = glob.glob(os.path.join(_path, "*.txt"), recursive=True)
		documents =  all_docs_txt

		'''Tenemos el path y la lectura de cada documento'''
		docs_text = [(doc_path,read_doc(doc_path)) for doc_path in documents]
		
		'''Mandamos a procesar cada documento'''
		for i in range(len(docs_text)):

			json_process = json.dumps({'action':'process', 'data':docs_text[i][1]})
			terms = json.loads(text_processing(json_process))['terms']

			'''Guerdamos los terminos ya procesados'''
			docs_text[i] = (docs_text[i][0], terms)
		
		'''construimos el diccionario en json correspondientes a los terminos de los documentos'''
		for doc in docs_text:
			terms = doc[1]
			doc_name = os.path.basename(doc[0])
			add_terms(doc_name, terms, data)

		'''Annadimos el idf de cada termino'''
		add_idfs(data, len(documents))
		'''Annadimos el peso de cada termino por cada documento'''
		add_w(data,0)
		
		'''El diccionario construido anteriormente lo guardaremos en la variable global dictionary'''
		json_process = json.dumps({'action':'create', 'data':data})
		utils.start(json_process)

	else: raise Exception("The path is not correct")


def query(query):

	'''Mandamos a procesar la consulta'''
	json_process = json.dumps({'action': 'process', 'data': query})
	query_terms = json.loads(text_processing(json_process))['terms']

	query_data = []

	'''construimos el diccionario en json correspondientes a los terminos de la consulta'''	
	add_terms('query',query_terms,query_data)
	'''Annadimos el idf a los terminos de la consulta'''
	add_idfs(query_data, 1)
	'''Annadimos el peso'''
	add_w(query_data,0.5)

	'''Buscamos la similitud de la consulta con los documentos'''
	dicc_ranking = sim(query_data,query_terms) 

	'''Ordenamos descendentemente por la similitud '''
	result= list(zip(dicc_ranking.keys(), dicc_ranking.values()))
	result.sort(key=lambda x: x[1], reverse=True)
	'''Nos quedamos con los n documentos que nos pidieron que mas similitud tienen'''
	#result = result[:count_doc]

	return json.dumps({'action':'report', 'sucess':True,'results':[{'document':dc, 'value':val} for dc, val in result if val >= 0.09]})



