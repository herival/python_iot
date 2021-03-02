#! /usr/bin/python3
"""
    Lire un  texte
    Noter le nombre d'occurence des mots
    Donner les 10 mots les plus fréquents
    Exporter l'histogramme (mot, nbre d'occurences) en CSV
"""
import sys

#Ne pas prendre en compte les mots trop courts car ils sont les plus fréquents
MINLEN=5


#Initialiser un dictionnaire
d={}


#Préparer une table de correspondance pour substituer les caractères
#de ponctuation et autres séparateurs par des espaces
intab=",.;!?()[]{}\'/`\""+"\u2019\u2018"
#Unicode 2019 et 2018 sont des apostrophes courbes, fermante et ouvrante respectivement
#for c in intab: print(c) #debug
outtab=" "*len(intab)
trantab=str.maketrans(intab,outtab)



#Ouvrir le fichier d'entrée
try:
    filename="testinput.txt"
    fi=open(filename, "r", encoding="utf-8")
except Exception as e:
    print("Cannot read file "+filename)
    print("Reason: ",e)
    sys.exit(1)



#Traitement ligne par ligne
try:
    nlinei=0    #noter les numéros des lignes lues
    nword=0    #noter le compte des mots
    for l in fi:   #pour chaque ligne du fichier d'entrée
        #éliminer les marques de ponctuation et tout mettre en minuscules
        nlinei+=1
        for w in l.translate(trantab).lower().split():
            nword+=1
            """if w in d and len(w)>MINLEN:
                d[w]+=1
            else:
                d[w]=1 """
            if len(w)> MINLEN:
               d[w]=(d.get(w,0))+1
except Exception as e:
    print("Failed to read line #"+str(nline))
    print("Reason: ",e)
    fi.close()
    sys.exit(1)

    

#Fermer le fichier d'entrée
fi.close()



#10 mots les plus fréquents
#trier le dictionnaire par les valeurs et slicer les 10 dernières, et les retourner
#pour que le plus fréquent soit en tête

#Trier par les valeurs n'est pas trivial...
#le 2nd argument à sorted est une fonction d'une variable.
#Appliquée à chaque élément du conteneur à trier, elle donne la valeur de la clé du tri
#Cela correspond à la méthode __getitem__ de l'objet dictionnaire.

#Trier par valeurs décroissantes est prévu par sorted.
#Un 3ème argument à sorted est un booléen qui dit que l'on veut un tri décroissant
#Cela aurait pu être utilisé ici (reverse=True) et la slice aurait été [:10] sans
#qu'il n'y ait besoin de la retourner

sd=sorted(d, key=d.__getitem__)[-10:][::-1]
#afficher les mots et leur nbre d'apparitions
for w in sd:
    print(w, d[w], sep="\t")




#créer le fichier de sortie CSV
try:
    filename="testoutput.csv"
    fo=open(filename, "w")
except:
    print("Cannot open for write ", filename)
    print("Reason: ",e)
    sys.exit(1)

#écrire les mots dans l'ordre alphabétique, à raison d'un par ligne
# le mot, le séparateur ";" et son nombre d'occurences
try:
    nlineo=0
    for w in sorted(d):
        fo.write(w+";"+str(d[w])+"\n")
        nlineo+=1
except Exception as e:
    print ("Failed at writing word",w,"at line", nlineo)
    print("Reason",e)
    fo.close()
    sys.exit(1)
fo.close()

#afficher un bilan
print("Lignes lues : ", nlinei)
print("Mots lus : ", nword)
print("Mots différents retenus : ", len(d))

#dire que cela s'est bien passé
sys.exit(0)

        
        

        
