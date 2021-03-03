def show_call(fonction):
    # pour du multiple argument fonction_modifiée(*args, *kwargs):
    # reste plus qu'à boucler sur les arges et les kwargs
    # for a in args:
    #     if s:
    #         s+=","
    #     s+= a
    def fonction_modifiee(a, b):
        print("convertir", a, b)
        return fonction(a, b)
    return fonction_modifiee


@show_call
def convertir(montant, taux):
    print(taux*montant)

# devise1 = EUR
# devise2 = USD
# tauxdechange = 0.9
# montantaconvertir = 100
# devise1 = input("Devise d'origine : ")
# devise2 = input("Devise d'arrivée : ")
tauxdechange = float(input("Taux de change : "))
montantaconvertir = float(input("Montant à convertir : "))

# print(montantaconvertir,
#       devise1,
#       "=",
#       convertir(montantaconvertir,tauxdechange),
#       devise2)

convertir(tauxdechange, montantaconvertir)

