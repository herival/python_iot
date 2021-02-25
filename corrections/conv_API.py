import urllib.request
import json
def conv(taux, montant):
    """fonction qui converti des euros en dollars"""
    return montant*taux

# Debut Main !

import urllib.request
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
r = opener.open("https://www.freeforexapi.com/api/live?pairs=EURUSD").read()
#print(r)
monjson = json.loads(r)
taux_EUR_USD =float(monjson["rates"]["EURUSD"]["rate"])
print("Devise à convertir : EUR vers USD")
print("Voici le montant converti en USD",conv(float(input("Entrez un montant en Euro à convertir en Dollars ? ")),taux_EUR_USD),"au taux de",taux_EUR_USD)


