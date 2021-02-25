# tuple et operateur sur les sequences
texte = "Test d'un tuple"
untuple = ("test", 3, 5, 2, "tuple")
print(texte.index("e"))
print(untuple.index(3))

# slicing
print(texte[2:])
print(texte[2:4])

# exercices 
mon_texte='anticonstitutionnellement'
chiffre = list(range(10))
print(chiffre)

print(chiffre[0:6]) # chiffre 1 ~ 5 peut aussi s'écrire [:6]
print(mon_texte[0:4]) # anti [:4]
print(mon_texte[4:16]) # consitution
print(chiffre[0:10:2]) # chiffre 0 2 4 6 8 [::2]
print(mon_texte[::-1])  # a l'envers [-1::-1]
print(chiffre[3::4]) # 3, 7
print(chiffre[::-2])  # a l'envers par 2 [-1::-2]
print(chiffre[1::2][::-1])  # slicer le resultat du slice

