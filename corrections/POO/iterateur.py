    
class Iterateur:
    def __init__(self):
        pass
    def __iter__(self):
        pass
        return self
    def __next__(self):
        …
        return xx #la valeur suivante
        …
        raise StopIteration

for i in iterateur(x):