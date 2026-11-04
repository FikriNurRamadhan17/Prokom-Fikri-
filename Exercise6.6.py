# Exercise 6.6
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}
people = ['jen', 'fikri', 'phil', 'budi']

for person in people:
    if person in favorite_languages.keys():
        print(f"Thank you for responding, {person.title()}!")
    else:
        print(f"{person.title()}, please take our poll!")