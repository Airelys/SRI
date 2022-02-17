from numpy import e
import model
import evaluation_measures
import json
import expansion_query

path = 'C:/Users/Airelys/Desktop/med/'

json_value = json.dumps({'action': 'build', 'path': path})

model.model(json_value)

file = open('C:/Users/Airelys/Desktop/medquery.txt','r')


p = 0
r = 0
f = 0
f1 = 0
f2 = 0
rp = 0
fa = 0

count = 1
for item in file:
    rr = []
    rel = []
    r10 = []
    rr10 = []

    if item != '\n':
        json_value = json.dumps({'action': 'query', 'query': item})

        json_result = json.loads(expansion_query.start(json_value))

        for pair in json_result['results']:
            if(len(r10) < 10):
                r10.append(pair["document"])
                
            file2 = open('C:/Users/Airelys/Desktop/medqrel.txt','r')
            for j in file2:
                b =''
                t = 3
                for i in j:
                    if i ==' ':
                        break
                    b+=i
                    t+=1
                if (str(count) == str(b)):
                    a =''
                    for i in j[t:]:
                        if i ==' ':
                            break
                        a+=i
                    rel.append(a)
                    if (pair["document"] == (str(a) + ".txt")):
                        if (len(r10) < 10):
                            rr10.append(a)
                        rr.append(a)
        if len(json_result['results'])>=1:
            
            count += 1
            p += evaluation_measures.precision(len(rr),len(json_result['results']))
            r += evaluation_measures.recall(len(rr),len(rel)/len(json_result['results']))
            f += evaluation_measures.measure_f(len(rr),len(json_result['results']),len(rel)/len(json_result['results']),0)
            f2 += evaluation_measures.measure_f(len(rr),len(json_result['results']),len(rel)/len(json_result['results']),2)
            f1 += evaluation_measures.measure_f1(len(rr),len(json_result['results']),len(rel)/len(json_result['results']))
            rp += evaluation_measures.r_precision(len(rr10),10)
            fa += evaluation_measures.fallout(len(json_result['results']),len(rel)/len(json_result['results']),len(rr),1400)
        
    

print(p/30)
print(r/30)
print(f/30)
print(f1/30)
print(f2/30)
print(rp/30)
print(fa/30)