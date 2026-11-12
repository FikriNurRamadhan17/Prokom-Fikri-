# Exercise 9-14
from random import choice

pilihan = [3, 7, 12, 25, 41, 56, 68, 74, 88, 91, 'a', 'b', 'c', 'd', 'e']

pemenang = []
while len(pemenang) < 4:
    kandidat = choice(pilihan)
    if kandidat not in pemenang:   # supaya tidak ada yang kembar
        pemenang.append(kandidat)

print(f"Tiket yang cocok dengan {pemenang} menang hadiah!")