# Exercise 10-11 (penulis)
from pathlib import Path
import json

number = int(input("Berapa angka favoritmu? "))

path = Path('favorite_number10_11.json')
path.write_text(json.dumps(number))