# Exercise 10-5
from pathlib import Path

path = Path('guest_book.txt')
isi = ""

while True:
    name = input("Masukkan namamu (ketik 'q' untuk berhenti): ")
    if name == 'q':
        break
    isi += f"{name}\n"
    print(f"Halo, {name}! Namamu sudah dicatat.")

path.write_text(isi)
