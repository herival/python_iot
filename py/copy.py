import copy as cp
liste1 = ["Bla", "bli", "blo", 4]

liste2 = liste1 # affecte liste1 sur liste2
liste2 = cp.copy(liste1) # copie de la liste Juste à un niveau
liste2 = liste1[:] # copie le slice de liste1 et n'affecte pas la liste 1
#deepcopy pour copier sans les liens des objets, dissocier totalement