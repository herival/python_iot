from math import sqrt

def trinome(a,b,c,x):
    return a*x**2+b*x+c

def solve(a, b, c):
    #discriminant
    d=b*b-4*a*c
    if d>0:
        xi=(-b-sqrt(d))/(2*a)
        xii=(-b+sqrt(d))/(2*a)
        return xi,xii
    elif d==0:
        return -b/(2*a)
    else:
        #pas de racine, pas de return
        #equivaut à return None
        pass


def residu (a,b,c):
    r = solve (a, b,c)
    if r is None:
        pass
    elif type(r) is float:
        return trinome(a,b,c,r)
    else:
        x1,x2=r
        return trinome(a, b, c, x1), trinome(a,b,c, x2)

a= 1
b=-2
c= -8
print(solve(a, b, c))
print(residu(a,b,c))
