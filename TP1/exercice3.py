
distancekm = float(input("Entrez la distance en km : "))
tempsmin = float(input("Entrez le temps en min: "))

distancem = distancekm * 1000
tempss = tempsmin * 60
vitesse = distancem / tempss

print(f"La vitesse est de {vitesse:.2f} m/s.")
