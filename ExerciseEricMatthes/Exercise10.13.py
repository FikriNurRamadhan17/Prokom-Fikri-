# Exercise 10-13
from pathlib import Path
import json

path = Path('user_info10_13.json')

if path.exists():
    user = json.loads(path.read_text())
else:
    user = {
        'nama': input("Siapa namamu? "),
        'umur': input("Berapa umurmu? "),
        'kota': input("Tinggal di kota mana? "),
    }
    path.write_text(json.dumps(user))
    print("Datamu sudah kusimpan.")

print("\nYang kuingat tentangmu:")
for key, value in user.items():
    print(f"- {key}: {value}")