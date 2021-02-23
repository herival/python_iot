
devise1=(input("Devise d'origine: "))
devise2=(input("Devise destination: "))
taux=float(input("Taux: "))
montant=float(input("Montant: "))

conversion = taux * montant
print(montant ,devise1 , " = " , conversion, devise2)