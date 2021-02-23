# recursive (appelle la même fonction dans la fonction)
def factorielle(n):
    if n<2: 
        return 1
    else:
        return(n * factorielle(n-1))
    
print(factorielle(4))

# autre manières : 
def fac_recu(n):
    if n:
        return n*fac_recu(n-1)
    else:
        return 1
print(fac_recu(4))

#iterative 

def fac(m):
    resultat = 1
    for i in range(1,m+1):
        resultat = resultat * i
    return resultat

print(fac(3))

