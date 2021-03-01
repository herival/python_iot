
def premier(N):
    liste=[]
    for i in range(N+1):
        if i > 1: 
            for j in range(2,i):
                if(i%j)==0:
                    break
                else:
                    liste.append(i)
    return liste

print(premier(1))