
nbr1 = float(input("Entrez le 1er nombre : "))
nbr2 = float(input("Entrez le 2eme nombre : "))
operation = input("Choisissez une opération (+, -, *, /) : ")
if operation == "+":
    print(f"Le résultat de l'addition est :{nbr1 + nbr2}")
elif operation == "-":
    print(f"Le résultat de la soustraction est :{nbr1 - nbr2}")
elif operation == "*":
    print(f"Le résultat de la multiplication est :{nbr1 * nbr2}")
elif operation == "/":
    if nbr2 != 0:
        print(f"Le résultat de la division est :{nbr1 / nbr2}",)
    else:
        print("Division par zéro n'est pas autorisée")
else:
    print("Opération invalide.")
