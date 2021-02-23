# exercice pgcd trouver l'agorithme
# recursive
# PGCD(b,a%b)
# exercice Trinome ax2+ bc + c

# fonction convertisseur devises

def pgcd(a, b):
    if b > 0:
        reste = a % b
        return pgcd(b, reste)
    else:
        return a


print(pgcd(64, 38))
