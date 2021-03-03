# recurcif
def fib_r(n):
    global compteur
    compteur += 1
    if n < 2:
        return n
    return(fib_r(n-1)+fib_r(n-2))

compteur = 0
print(fib_r(10), compteur)

# for i in range(10):
#     print(fib_r(i))
