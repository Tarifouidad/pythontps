total_notes = 0
total_coefficients = 0

# Boucle pour saisir les notes et coefficients
for i in range(5):
    print(f"Matière {i+1}:")
    note = float(input("Saisir la note :"))
    coef = float(input("Saisir le coffecient :"))
    total_notes += note * coef
    total_coefficients += coef
moyenne = total_notes / total_coefficients
print(f"Moyenne de ces 4 notes : {moyenne:.2f}")
if moyenne >= 10:
    print("Semestre validé")
elif 7 <= moyenne < 10:
    print("Rattrapage")
else:
    print("Semestre non validé")
