import re
import json
import nltk
from nltk.tokenize import word_tokenize
nltk.download()
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from string import punctuation


'''Para mandar a procesar los datos'''
def text_processing (analyze_json):
    data = json.loads(analyze_json)
    if data['action'] == 'process':
        terms = _processing_(data['data'])
        return json.dumps({'terms': terms})

'''Palabras con apostrofes'''
patterns = [(r'[wW]on\'t', 'will not'),
            (r'[cC]an\'t', 'can not'),
            (r'[iI]\'m', 'i am'),
            (r'[aA]in\'t', 'is not'),
            (r'[iI]t\'s', 'it is'),
            (r'(\w+)\'ll', '\g<1> will'),
            (r'(\w+)n\'t', '\g<1> not'),
            (r'(\w+)\'ve', '\g<1> have'),
            (r'(\w+)\'s', '\g<1>'),
            (r'(\w+)\'re', '\g<1> are'),
            (r'(\w+)\'em', '\g<1> them'),
            (r'[nN]\'t', 'not'),
            (r'\'m', 'am'),
            (r'\'s', 'is'),
            (r'\'ll', 'will'),
            (r'\'ve', 'have'),
            (r'\'re', 'are')]

'''Para reemplazar las palabras abreviadas con apostrofes por su escritura completa'''
def _replace_( text):
    s = text
    for (pattern, repl) in patterns:
        s = re.sub(pattern, repl, s)
    return s

'''Cogemos los stopwords'''
_stopwords = stopwords.words('english')
'''Cogemos los signos de puntuacion'''
no_words = list(punctuation)


def _processing_(data):

    match = re.search(r'([a-zA-z]+)', data)

    if len(data)==0 or not match:
        return []

    '''Reemplazar palabras abreviadas'''
    data = _replace_(data)

    '''Tokenizacion'''
    tokens = word_tokenize(data)

    '''Eliminacion de stopwords'''
    tokens = [element for element in tokens if (element not in _stopwords and element not in no_words)]

    '''Stemming'''
    stems = SnowballStemmer('english') 
    tokens_stem = [stems.stem(token) for token in tokens]

    '''Devolvemos los tokens despues del procesamiento'''
    return tokens_stem


    
    
    