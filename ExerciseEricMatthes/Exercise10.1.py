# Exercise 10-1
from pathlib import Path

path = Path('learning_python.txt')

# Cara 1: baca seluruh isi sekaligus
contents = path.read_text()
print(contents)

# Cara 2: simpan baris dalam list, lalu loop
lines = contents.splitlines()
for line in lines:
    print(line)