# iterative

def fib_i(n):
    liste = []
    for i in range(n):
        if n > 1: 
            liste.append(n + (n-1))
            return liste
    return 0

print(fib_i(10))
# for i in range(10):   
#     print(fib_r(i))

