# nombre premier inférieur à N


def premier(N):
    liste = list(range(2, N))
    liste2= list(range(2,N))
    for i in range(2, N):
        # if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0 or i%11 == 0, or i%13==0 :
        if i % 2 == 0:
            liste.remove(i)
    for i in liste:
        a = 0
        for ==0:
            liste.remove


            

    # for j in range(101, N):
    #     for i in liste:
    #         if j in liste and j % i == 0:
    #             # liste.remove(j)
    #             return i

    return liste


print(premier(200))
# print(a)

print(75 % 5)
