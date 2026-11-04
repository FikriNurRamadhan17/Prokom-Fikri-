# Exercise 6.8
pet_1 = {'kind': 'kucing', 'owner': 'Fikri'}
pet_2 = {'kind': 'anjing', 'owner': 'Budi'}
pet_3 = {'kind': 'kelinci', 'owner': 'Sari'}

pets = [pet_1, pet_2, pet_3]
for pet in pets:
    for key, value in pet.items():
        print(f"{key}: {value}")
    print()
    