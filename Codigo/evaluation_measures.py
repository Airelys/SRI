
'''Calculamos la presicion'''
def precision(RR, REC):
    try:
        if REC==0:
            raise Exception()
        return RR/REC
    except (Exception):
        print("Cero Documentos recuperados.")

'''Calculamos el recobrado'''
def recall (RR, REL):
    try:
        if REL==0:
            raise Exception()
        return RR/REL
    except (Exception):
        print("Cero Documentos recuperados.")

'''Calculamos la medida de f'''
def measure_f (RR, REC, REL, beta):
    P = precision(RR, REC)
    R = recall(RR, REL)
    if(((beta**2)*P) + R) != 0:
        return ((1+ beta**2)*P*R) / (((beta**2)*P) + R)
    return 0
       

'''Calculamos la medida de f1'''
def measure_f1 (RR, REC, REL):
    P = precision(RR, REC)
    R = recall(RR, REL)
    if (P + R) != 0:
        return 2*P*R / (P + R)
    return 0

'''Calculamos r-presicion'''
def r_precision (RR, R):
    return RR / R

'''Calculamos la proporcion de fallo'''
def fallout (REC, REL, RR, TOTAL):
    return (REC-RR)/(TOTAL - REL)

