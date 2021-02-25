def convertir(montant, taux):
    return taux*montant

devise1 = input("Devise d'origine : ")
devise2 = input("Devise d'arrivée : ")
tauxdechange = float(input("Taux de change : "))
montantaconvertir = float(input("Montant à convertir : "))

print(montantaconvertir,
      devise1,
      "=",
      convertir(montantaconvertir,tauxdechange),
      devise2)

