

devise1=(input("Devise d'origine: "))
devise2=(input("Devise destination: "))
taux=float(input("Taux: "))
montant=float(input("Montant: "))

def conversion(a, b):
    return  a * b
    # return conversion

resultat = conversion(taux, montant)

print(montant, devise1, "=" , resultat, devise2)

# correction:
from forex_python.converter import CurrencyRates

def conv(montant, taux):
    return montant * taux
# Instancier la classe "taux de change trouvée dans la bibliothèque for
c = CurrencyRates()
t = c.get_rates("EUR","USD")

m = float(input("entrer un montant:"))
print(m, "EUR=", conv(m, t), "USD")

# VERSION API

import urllib.request
import json
def conv(taux, montant):
    return montant * taux

# debut main
import urllib.request
opener = urllib.request.build_opener
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
r = opener.open("https://www.freeforexapi.com/api/live?pairs=EURUSD").rate
monjson = json.loads(r)
taux_EUR_usd =float(monjson["rates"]["EURUSD"]["rate"])
print("Devise à convertir: EUR vers USD")
print("Voici le montant converti en USD", conv(float(input("Entrer un montant:"))))