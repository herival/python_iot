from liste import *

def deuxieme(a):
    
    rest = reste(a)
    return (prem(rest))

# def troisieme(a):
#     for i in [0,1]:
#         a = reste(a)
#     return (prem(a))
def troisieme(a):
    return (prem(reste(reste(a))))



# def dernier(a):
#     for i in reste(a): # total des éléments moins un (le premier)
#         a = reste(a) 
#     return (prem(a))

def dernier(a):

    if vide(reste(a)):
        return (prem(a))
    else:
        return dernier(reste(a))


def test(a):
    return vide(a)

compteur = 0
def cardinal(a):
    if vide(a):
        return 0
    else:
        compteur += 1
        if vide(reste(a)):
            return compteur
        else:
            cardinal(reste(a))


liste = ["premier", "deuxième", "troisième", 'quatrième', 'cinquième']

print(deuxieme(liste))
print(troisieme(liste))
print(dernier(liste))

print(cardinal(liste))