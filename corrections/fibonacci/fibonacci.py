# recurcif

def fib_r(n):
    if n>1:
        return fib_r(n+ (n-1)) 
    elif n == 1:
        return 1
    else:
        return 0

print(fib_r(3))
# for i in range(10):   
#     print(fib_r(i))

