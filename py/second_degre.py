
val_a=int(input("entrer a: "))
val_b=int(input("entrer b: "))
val_c=int(input("entrer c: "))

def second_degre(a, b, c):
    delta = (b*b)-(4*a*c)
    if delta > 0:
        x1 = (-b - (delta**(1/2)))/2*a
        x2 = (-b + (delta**(1/2)))/2*a
        return("x1=", x1, "x2 =", x2)
    elif delta == 0:
        return("x =" -b / (2*a))
    else :
        return("pas de reponse")

print(second_degre(val_a, val_b, val_c))