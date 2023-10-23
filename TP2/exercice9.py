taux_euro = 10.86
taux_mad = 0.092
print("Choisissez la direction de conversion :")
print("1. Euro en Dirham (EUR -> MAD)")
print("2. Dirham en Euro (MAD -> EUR)")
choix = input("Entrez 1 ou 2 : ")
if choix == "1":
    direction = "EUR -> MAD"
    taux = taux_mad
elif choix == "2":
    direction = "MAD -> EUR"
    taux = taux_euro
else:
    print("Choix invalide. Le programme se termine.")
    exit()
valeurs_converties=[]
while True:
    valeur = float(input(f"Entrez une valeur en {direction} (saisissez un nombre négatif pour arrêter) : "))
    if valeur < 0:
        break
    valeur_convertie = valeur * taux
    valeurs_converties.append(valeur_convertie)
print(f"Valeurs converties en {direction} :")
for valeur in valeurs_converties:
    print(valeur)