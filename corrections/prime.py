N = 100
prime=set() # 

def is_prime(x):
    for p in prime:
        if x%p==0:
            return False
    return True

for i in range(2, N+1):
    if is_prime(i):
        prime |={i} # ajouter i dans l'ensemble des nombres premiers, pareil que prime.append

print(prime)
print(sorted(prime))