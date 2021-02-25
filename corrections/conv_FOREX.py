# Utilisez la commande ci-dessous pour installer la bibliothèque
# pip install forex_python
from forex_python.converter import CurrencyRates

def conv(montant, taux):
    return montant * taux

#Instancier la classe "taux de change" trouvée dans la bibliothèque forex...
c = CurrencyRates()

#Demander à l'utilisateur la devise de départ
devise1 = input("Quelle devise souhaitez vous convertir (ex:EUR) ? ")
#Demander à l'utilisateur la devise d'arrivée
devise2 = input("Quelle devise souhaitez vous obtenir (ex:USD) ? ")

#Obtenir le taux actuel de la devise 1 vers la devise 2
taux = c.get_rate(devise1,devise2)

#Demander à l'utilisateur quel montant doit être converti
montant = float(input("Entrez un montant :  "))

print(montant, devise1, "=" , conv(montant, taux), devise2)
