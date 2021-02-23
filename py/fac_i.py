def fac_i(n):
    """
        Factorielle n par un algorithme itératif
    """
    f=1
    for k in range (2,n+1):
     f*=k
    return f

        


for i in range(10):
    print (fac_i(i))

fac_i(0) => 1

fac_i(3)

    un element compris (2,3)
        f = 1 * 2 = 2
        f = 2 * 3 = 6
        
