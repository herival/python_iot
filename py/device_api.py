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