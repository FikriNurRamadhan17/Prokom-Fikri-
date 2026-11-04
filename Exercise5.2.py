# Exercise 5.2
name = 'Fikri'
print(name == 'Fikri')              # True
print(name == 'Budi')               # False
print(name != 'Budi')               # True
print(name != 'Fikri')              # False

print(name.lower() == 'fikri')      # True
print(name.lower() == 'FIKRI')      # False

age = 19
print(age == 19)                    # True
print(age == 20)                    # False
print(age != 20)                    # True
print(age != 19)                    # False
print(age > 18)                     # True
print(age > 19)                     # False
print(age < 20)                     # True
print(age < 19)                     # False
print(age >= 19)                    # True
print(age >= 20)                    # False
print(age <= 19)                    # True
print(age <= 18)                    # False

print(age > 18 and age < 25)        # True
print(age > 18 and age < 19)        # False
print(age > 25 or age == 19)        # True
print(age > 25 or age < 10)         # False

fruits = ['apel', 'jeruk', 'mangga']
print('apel' in fruits)             # True
print('pisang' in fruits)           # False
print('pisang' not in fruits)       # True
print('apel' not in fruits)         # False
