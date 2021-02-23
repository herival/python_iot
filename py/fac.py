def fac(n):
    if n:
        return n*fac(n-1)
    else:
        return 1

print(fac(3))
