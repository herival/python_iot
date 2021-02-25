
def match(listes, pattern):
    for i in listes:
        if pattern not in i:
            continue
        else:  
            return True
    return False

# methode 2
def match2(listes, pattern):
    for i in listes:
        if pattern in i:
            return True
    return False

# methode raccourci avec comprehension, 
# l'algo cherche le True dans le [pattern in mot for mot in liste]
def match3(listes, pattern):
    return True in [pattern in mot for mot in listes]


liste_mot = ['riri','fifi','loulou']

print(match(liste_mot,'blo'))
print(match(liste_mot,'lou'))
print(match(liste_mot,'fif'))
print(match(liste_mot,'riag'))
print(match3(liste_mot,'loulou'))