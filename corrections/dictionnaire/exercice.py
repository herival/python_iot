import string
import csv
import os # pour mettre un chemin, gerer les repertoires

with open('testinput.txt', 'r', encoding="utf-8") as f:

    data = f.read()
    # on peut aussi ecrire
    # data = "".join(f.readline())
    print(len(data))
    f.close()
    texte = data
    for punc in string.punctuation: 
        texte = texte.replace(punc, " ") # remplace toutes les ponctuation de string.punctuation
        
    texte = texte.lower()
    texte2 = (texte.split()) # supprime tout les espaces et convertit en liste

    texte3=[]
    for word in texte2:
        if len(word)>4:
            texte3.append(word)

    compte = {k: texte3.count(k) for k in set(texte3)}

    texte_trie = sorted(compte.items(), key=lambda x: x[1], reverse=True)

    fichier_csv = open('texte.csv', 'w')
    mywriter = csv.writer(fichier_csv, delimiter=';', dialect='excel')
 
    for k,y in compte.items():
        mywriter.writerow([k,y])
 
    fichier_csv.close()

    print(texte_trie[0:9])
    
    
    # print(len(texte2))
    print(len(texte3))
    print(len(compte))

