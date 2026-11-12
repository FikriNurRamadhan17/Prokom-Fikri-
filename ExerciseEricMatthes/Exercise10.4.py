# Exercise 10-4
from pathlib import Path

name = input("Siapa namamu? ")

path = Path('guest.txt')
path.write_text(name)

print(f"Terima kasih, {name}. Namamu sudah dicatat.")
