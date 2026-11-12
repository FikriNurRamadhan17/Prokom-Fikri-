# Exercise 9-15
from random import choice

pilihan = [3, 7, 12, 25, 41, 56, 68, 74, 88, 91, 'a', 'b', 'c', 'd', 'e']
my_ticket = [7, 25, 'b', 'e']


def undi():
    """Undi 4 elemen berbeda."""
    hasil = []
    while len(hasil) < 4:
        kandidat = choice(pilihan)
        if kandidat not in hasil:
            hasil.append(kandidat)
    return hasil


percobaan = 0
while True:
    percobaan += 1
    hasil = undi()
    if set(hasil) == set(my_ticket):
        break

print(f"Tiketmu menang setelah {percobaan} kali undian.")