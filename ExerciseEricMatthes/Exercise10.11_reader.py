# Exercise 10-11 (pembaca)
from pathlib import Path
import json

path = Path('favorite_number10_11.json')
number = json.loads(path.read_text())

print(f"Aku tahu angka favoritmu! Yaitu {number}.")
