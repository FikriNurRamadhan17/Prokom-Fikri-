# Exercise 6.10
favorite_numbers = {
    'fikri': [17, 8],
    'budi': [7, 21, 3],
    'sari': [3, 9],
    'andi': [21, 5],
    'dimas': [9, 1, 4],
}
for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(number)