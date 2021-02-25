# nombre premier inférieur à N

a = list(range(0, 100))


def premier(N):
    liste = list(range(11, N))

    for i in range(11, 100):
        if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
            liste.remove(i)

    # for j in range(101, N):
    #     for i in liste:
    #         if j in liste and j % i == 0:
    #             # liste.remove(j)
    #             return i

    return liste


print(premier(200))
# print(a)

print(75 % 5)
