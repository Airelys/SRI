from nltk.corpus import stopwords
from string import punctuation
from nltk import wordpunct_tokenize
import json
import model
from nltk.corpus import wordnet 



def start(json_request):

    data = json.loads(json_request)
    
    '''Buscamos los sinonimos de los terminos de la consulta'''
    words = data['query'] + " " + synonyms(data['query'])
    
    '''Mandamos a ejecutar el modelo con los sinonimos tambien'''
    return model.query(words)


'''Metodo para buscar los sinonimos de la consulta'''
def synonyms(data):

    the_stopwords = stopwords.words('english')
    no_words = list(punctuation)

    tokens = wordpunct_tokenize(data)

    tokens = [elem for elem in tokens if (elem not in the_stopwords and elem not in no_words)]

    words=[]
    synonyms = []
    for token in tokens:
        for syn in wordnet.synsets(token):
            for lm in syn.lemmas():
                synonyms.append(lm.name())

        synonyms = (set(synonyms))
        words.extend(list(synonyms)[:2])
        synonyms = []

    return " ".join(words)