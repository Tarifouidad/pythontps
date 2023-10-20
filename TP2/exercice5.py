def inserer (L,val):
    i=0
    while i<len(L) and L[i]<val:
        i+=1
    L.insert(i,val)
L=[1,3,5,7,9]
inserer(L,4)
print(L)