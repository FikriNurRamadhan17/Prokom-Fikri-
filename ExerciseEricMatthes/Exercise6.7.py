# Exercise 6.7
person_1 = {'first_name': 'Fikri', 'last_name': 'Ramadhan', 'age': 19, 'city': 'Surakarta'}
person_2 = {'first_name': 'Budi', 'last_name': 'Santoso', 'age': 20, 'city': 'Jakarta'}
person_3 = {'first_name': 'Sari', 'last_name': 'Dewi', 'age': 18, 'city': 'Bandung'}

people = [person_1, person_2, person_3]
for person in people:
    for key, value in person.items():
        print(f"{key}: {value}")
    print()