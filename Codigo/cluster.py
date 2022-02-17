import pandas 
import nltk
import re
import os
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

stopwords = stopwords.words('english')
stemmer = SnowballStemmer("english")

titles = []
texts = []

tfidf_vector = None
tfidf_matrix = None

kmeans = None
cluster = None
frame = None
docs = None
doc_clust = {}
clust_docs = {}

'''Dentro del path cogemos todos los documentos y el texto que contienen'''
def _load_(path):
    if os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            for filename in files:
                with open(os.path.join(root,filename), encoding='utf8', errors='ignore') as f:
                    titles.append(filename)
                    texts.append(f.read())

'''Tokenizamos y lematizamos el texto'''
def _tokenize_and_stemmer_(text):
    tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    for token in tokens:
        if re.search('[a-zA-Z]',token):
            filtered_tokens.append(token)
    stems = [stemmer.stem(t) for t in filtered_tokens]
    return stems


'''Calculamos el peso de los documentos y a partir de ahi la semejanza que estos tienen'''
def _tf_idf_():
    global tfidf_vector, tfidf_matrix
    tfidf_vector = TfidfVectorizer(max_df=0.8, max_features=200000000, min_df=0.2, stop_words='english',use_idf=True,tokenizer=_tokenize_and_stemmer_,ngram_range=(1,3))
    tfidf_matrix = tfidf_vector.fit_transform(texts)

'''Creamos los clusters a partir del metodo kmeans'''
def _clustering_(num_clusters):
    global kmeans,clusters,frame,docs
    kmeans = KMeans(n_clusters=num_clusters)
    kmeans.fit(tfidf_matrix)
    clusters = kmeans.labels_.tolist()
    docs =  {    
            'title' : titles, 
            'text' : texts,
            'cluster':cluster
            }
    frame = pandas.DataFrame(docs,index=[clusters],columns=['title','cluster'])
    frame['cluster'].value_counts()        

'''Para  nombrar los clusters y agrupar los documentos en su respectivo cluster'''
def _printer_(num_clusters): 

    for i in range(num_clusters):
        doc_list = []
        label_list = []
        
        label_list.append("Cluster:" + str(i+1))
             
        for title in frame.loc[i]['title'].values.tolist():
            doc_list.append(title)
            doc_clust[title] = i
        clust_docs[i] = (doc_list,label_list)


'''Devuelve el cluster del documento'''
def all_label_from_cluster(doc_name):
    result = ""
    for item in clust_docs[doc_clust[doc_name]][1]:
        result += item +" "
    return result


'''Manda a ejecutar los metodos para construir los clusters'''
def clustering(path,num_clusters):
    _load_(path)            
    _tf_idf_()
    _clustering_(num_clusters)
    _printer_(num_clusters)
    