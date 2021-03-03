# iterative

def fib_i(N):
    assert N>=0, "N doit être positif" # condition pour lever une exeption: si N est pas positif il renvoi l'exeption en message
    global compteur
    x = 1
    y = 1
    z = 0
    if N == 0:
        compteur +=1
        return 0
    elif N <= 2:
        compteur +=1
        return 1
    for i in range(N-2):
        compteur +=1
        z = x+y
        (x, y) = (y, z)

    return z

compteur = 0
# print(fib_i(10), compteur)
for i in range(10):
    print(fib_i(i), compteur)
