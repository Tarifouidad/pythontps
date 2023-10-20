
user_input = input("Saisissez une liste de nombres séparés par des espaces : ")
numbers = [int(num) for num in user_input.split()]
number_to_remove = int(input("Saisissez le nombre à supprimer : "))
filtered_numbers = [num for num in numbers if num != number_to_remove]
print("Liste après suppression :", filtered_numbers)
