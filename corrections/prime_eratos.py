import time
start_time = time.time()

def nombrepremier(n):
    listNbPremier = [True for i in range(n)]
    listNbPremier[0]=False
    listNbPremier[1]=True
    for i in range(n):
        if listNbPremier[i]:
            listNbPremier[i*i::i]=[False]*len(listNbPremier[i*i::i])
    return listNbPremier

NOMBREPREMIERMAX = 100

print("les nombres premiers" nombrepremier(NOMBREPREMIERMAX))