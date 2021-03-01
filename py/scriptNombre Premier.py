import time
start_time = time.time()

def nombrepremier(n):
    listNbPremier = [True for i in range(n)]
    listNbPremier[0]= False
    listNbPremier[1]= False
    for i in range(n):
        if listNbPremier[i]:
            listNbPremier[i*i::i] = [False]*len(listNbPremier[i*i::i])
    return listNbPremier


NOMBREPREMIERMAX = 100000

print("Les nombres premiers inférieurs à ", NOMBREPREMIERMAX ,\
      " sont : ",[i for i, x in enumerate(nombrepremier(NOMBREPREMIERMAX)) if x == True])
print("--- %s secondes ---" % (time.time() - start_time))

"""

def nombreprem(n):
    vecDiv=[]
    vecPrem=[]
    for i in range(1,n+1):
        for j in range(1,i+1):
            if i%j==0:
                vecDiv.append(i)
        if vecDiv.count(i)==2:
            vecPrem.append(i)
    print(vecPrem)

start_time = time.time()
nombreprem(NOMBREPREMIERMAX)
print("--- %s secondes ---" % (time.time() - start_time))

"""

def estpremier (x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True

start_time = time.time()
primes=[]
for y in range(2,NOMBREPREMIERMAX):
    if estpremier(y):
        primes.append(y)
        #primes+=y

print(primes)

print("--- %s secondes ---" % (time.time() - start_time))
