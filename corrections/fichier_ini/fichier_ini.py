import configparser
import pdb


config = configparser.ConfigParser()
config.read('fichier.ini')
# print(config)
# print(config['precision']['test'])

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
    def convert(self, montant):
        return self.tx * montant

monconvertisseur = Convertisseur(config['convert']['devise1'],config['convert']['devise2'],float(config['convert']['taux']))
breakpoint()
# monconvertisseur2 = Convertisseur()

print(monconvertisseur)
print(repr(monconvertisseur))
print(monconvertisseur.convert(float(config['calcul']['montant'])))