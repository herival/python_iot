from math import sqrt as racine


def nPremier(MaxN):
    listeN = list(range(2, MaxN + 1))
    nombre = 2
    while nombre < racine(MaxN):
        for newNum in listeN:
            if newNum % nombre == 0:
                del(listeN[listeN.index(newNum)])
    return listeN


print(nPremier(200))
