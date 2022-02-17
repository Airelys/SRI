import json

'''Variable global en la que guerdaremos toda la informacion correspondiente 
a los terminos de los documentos'''
dictionary ={}

def start (json_request):

    json_data = json.loads(json_request)

    if json_data['action'] == 'create':
        _create_(json_data['data'])
    elif json_data['action'] == 'get':
        return _get_(json_data['key'])
    elif json_data['action'] == 'dict':
        return _dic_()

'''Para annadir una serie de terminos nuevos al diccionario'''
def _create_(data):
    for elem in data:
        key = elem['key']
        value = elem['value']
        dictionary[key] = value

'''Buscamos si un termino esta, si esta devolvemos su valor'''
def _get_(key):
    response = {}

    if key in dictionary:
        response['success'] = True
        response['value'] = dictionary[key]
    else:
        response['success'] = False
        response['value'] = None

    return json.dumps(response)


def _dic_():
    return json.dumps(dictionary)

