L = [1, 2, 5, 8, 6, 2, 5, 9, 1, 8, 8]
index=0
while index<len(L):
    if L.count(L[index])>1:
        L.pop(index)
    else:
        index+=1
print(L)

