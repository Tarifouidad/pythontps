L = [1, -30, 0, -2, 500, 4, 2, 100]
negatifs=[]
positifs=[]
for i in L:
    if i<0:
        negatifs.append(i)
    else:
        positifs.append(i)
M=negatifs+positifs
print(M)