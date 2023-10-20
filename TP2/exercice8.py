list = input("Saisissez une liste de nombres séparés par des espaces : ")
L = [int(num) for num in list.split()]
n=int(input("saisir un nombre :"))
i=0
occ=0
while i<len(L):
    if(L[i]==n):
       occ+=1
       print(f"{occ}:nombre d'occurence de {n} à la position {i+1}")
    i+=1