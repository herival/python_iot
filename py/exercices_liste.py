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

def cardinal(a):
    if vide(a):
        return 0
    else:
        return 1 + cardinal(reste(a)) # on peut incrementer sans créer de variable

def appartient(element, liste):
    if vide(liste):
        return False
    else:
        if element == prem(liste):
            return True
        else:
            return appartient(element, reste(liste))

def appartient_in(element, liste):  #maniere simple
    return element in liste

liste = ["premier", "deuxième", "troisième", 'quatrième', 'cinquième']

print(deuxieme(liste))
print(troisieme(liste))
print(dernier(liste))
print(appartient("premie", liste))
print(appartient_in("quatrième", liste))

print(cardinal(liste))