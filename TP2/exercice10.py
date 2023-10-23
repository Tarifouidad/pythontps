l1=input("saisir la 1er liste séparé par des espaces:")
L1 = [int(num) for num in l1.split()]
l2=input("saisir la 2 eme liste séparé par des espaces :")
L2 = [int(num) for num in l2.split()]
L3=list(set(L1) & set(L2))
print(L1)
print(L2)
print(L3)            