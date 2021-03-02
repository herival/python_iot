# iterative

def fib_i(N):
    x = 1
    y = 1
    z = 0
    if N == 0:
        return 0
    elif N <= 2:
        return 1
    for i in range(N-2):
        z = x+y
        (x, y) = (y, z)

    return z


# print(fib_i(10))
for i in range(11):
    print(fib_i(i))
