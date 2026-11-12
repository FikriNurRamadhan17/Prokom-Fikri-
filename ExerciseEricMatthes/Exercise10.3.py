# Exercise 10-3
from pathlib import Path

for line in Path('learning_python.txt').read_text().splitlines():
    print(line)
    