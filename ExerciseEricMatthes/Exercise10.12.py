# Exercise 10-12
from pathlib import Path
import json

path = Path('favorite_number10_12.json')

if path.exists():
    number = json.loads(path.read_text())
    print(f"Aku tahu angka favoritmu! Yaitu {number}.")
else:
    number = int(input("Berapa angka favoritmu? "))
    path.write_text(json.dumps(number))
    print("Oke, angka favoritmu sudah kuingat.")
    