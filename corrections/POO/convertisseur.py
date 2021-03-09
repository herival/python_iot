import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--devise1", type=str)
parser.add_argument("--devise2", type=str)
parser.add_argument("--taux", type=float)
args = parser.parse_args()
# print(args.taux)

class Convertisseur:
    def __init__(self, devise1="EUR", devise2="USD", taux=1.09):
        self.dev1 = devise1
        self.dev2 = devise2
        self.tx = taux
    def __str__(self):
        # return self.__repr__()
        return __class__.__name__
        # return 'Convertisseur de devise ' + self.dev1 + ' vers ' + self.dev2 +' au taux de '+  str(self.tx)
    def __repr__(self): # representation, créer une copie de l'objet
        # return '(' + self.dev1 + self.dev2 + str(self.tx) + ')'
        return "convertisseur('{}','{}',{})".format(self.dev1, self.dev2, self.tx)
    def convertir(self, montant):
        return self.tx * montant

monconvertisseur = Convertisseur(args.devise1,args.devise2, args.taux)
# monconvertisseur2 = Convertisseur()

print(monconvertisseur)
print(repr(monconvertisseur))
print(monconvertisseur.convertir(args.taux))

# # print(monconvertisseur2.convertir(50))
# print(monconvertisseur2)

# # surcharge
# class Convertisseur2(Convertisseur):
#     def __str__(self):
#         return f"Convertisseur de la devise{self.dev1} vers la devise {self.dev2}" #fprint

# obje3 = Convertisseur2()
# print(obje3)
# print(dir(Convertisseur))