def pgcd(p,q):
    while p%q:
        p,q=q,p%q
    return q


print(pgcd(5,15))

