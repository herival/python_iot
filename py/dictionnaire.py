dict_vide = {}
notes = {"pierre":15, "marie":13, "jean":14}
print(notes.keys())
print(notes.values())
print(notes['pierre'])
print(list(notes.keys()))

dico = [1, "bla", 3, "bla"]

#comprehension
# definir plusieurs instructions compacté
nom = [i for i in dico if i=="bla"]
print(nom)

# from random import randint
# N1 = 1000
# N2 = 9999

# sort() et sorted() trier
# les objets sont modifiables, exemple modifier l'objet print le surchagerai et on ne pourrait plus l'utiliser en tant que tel initialement.

