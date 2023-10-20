import random
n=random.randint(1,100)
print("Bienvenue dans le jeu de devinette !")
print("Vous avez 7 essais pour deviner le nombre entre 1 et 100.")
essaie=0
while essaie<7:
    nbr = int(input("Entrez votre devinette : "))
    if(n>1001 and n<1):
        print("oups,vous avez saisi un nombre eb dehors de l'intervalle")
    else:
        if nbr==n:
            print(f"Félicitations ! Vous avez trouvé le bon nombre aprés {essaie+1} essaie")
            break
        elif nbr < n:
            print(f"Le nombre est trop petit. Essais restants :{6-essaie}")
        else:
            print(f"Le nombre est trop grand. Essais restants :{6-essaie}")

        essaie += 1
