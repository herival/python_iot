# exercice pgcd trouver l'agorithme
# recursive
# PGCD(b,a%b)
# exercice Trinome ax2+ bc + c

# fonction convertisseur devises

def pgcd(a, b):

    reste = a%b

    if reste == 0:
        return b
    else:
        return pgcd(b, reste)

print(pgcd(4, 8))

# Correction

def pgcd2(p,q):
    if not p%q:
        return q
    else :
        return (pgcd2(q,p%q))