grade = input("Entrez le grade (A, B, C, D ou E) : ")
heures_travaillees = int(input("Entrez le nombre d'heures travaillées : "))
tarif_horaire = 0
prime = 0
if grade == 'A':
    tarif_horaire = 200
    prime = (heures_travaillees // 20) * 1000
elif grade == 'B':
    tarif_horaire = 150
    prime = (heures_travaillees // 20) * 800
elif grade == 'C':
    tarif_horaire = 120
    prime = (heures_travaillees // 15) * 500
elif grade == 'D':
    tarif_horaire = 100
    prime = (heures_travaillees // 15) * 350
elif grade == 'E':
    tarif_horaire = 80
    prime = (heures_travaillees // 10) * 100
else:
    print("Grade non valide")
salaire = (tarif_horaire * heures_travaillees) + prime
if tarif_horaire > 0:
    print("Le salaire de l'employé est de", salaire, "dh.")
