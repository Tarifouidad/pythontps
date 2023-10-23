l=input("saisir une liste separé par des espace :")
L=[int(num) for num in l.split()]
L_miroir=[]
for i in range(len(L)-1,-1,-1):
    L_miroir.append(L[i])
print("Liste transformé en miroir :",L_miroir)