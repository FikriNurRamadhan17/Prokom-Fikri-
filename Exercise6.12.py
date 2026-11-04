# Exercise 6.12
# Contoh: kembangkan 6-1 dengan menambah key baru
person = {
    'first_name': 'Fikri',
    'last_name': 'Ramadhan',
    'age': 19,
    'city': 'Surakarta',
}
person['major'] = 'Teknik Industri'
person['university'] = 'UNS'

for key, value in person.items():
    print(f"{key.title()}: {value}")