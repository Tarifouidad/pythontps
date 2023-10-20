poids = float(input("Entrez le poids en kilogrammes : "))
taille = float(input("Entrez la taille en mètres : "))
IMC = poids / (taille ** 2)
interpretation = None
if IMC > 40:
    interpretation = "Obésité morbide ou massive"
elif 35 <= IMC <= 40:
    interpretation = "Obésité sévère"
elif 30 <= IMC < 35:
    interpretation = "Obésité modérée"
elif 25 <= IMC < 30:
    interpretation = "Surpoids"
elif 18.5 <= IMC < 25:
    interpretation = "Corpulence normale"
elif 16.5 <= IMC < 18.5:
    interpretation = "Maigreur"
else:
    interpretation = "Famine"
print("Votre IMC est :", IMC)
print("Interprétation de l'IMC :", interpretation)
