# duck Typing
#  pour generaliser la fonction
# ex :
def getFrist(iterable, default = None):
    for x in iterable: 
        return x
    return default

print(getFrist('abc'))
print(getFrist({'ab':1, 'bc':2}))
