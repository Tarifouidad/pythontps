
s= int(input("Entrez le nombre de secondes : "))
h = s // 3600
min= (s% 3600) // 60
rest = (s % 3600) % 60


print(f"{s} secondes équivalent à {h}h {min}min {rest}sec.")