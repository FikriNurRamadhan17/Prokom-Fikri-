# Exercise 10-10
from pathlib import Path


def count_the(filename):
    """Hitung kemunculan 'the' dalam sebuah file teks."""
    path = Path(filename)
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"File {filename} tidak ditemukan.")
        return

    teks = contents.lower()
    tanpa_spasi = teks.count('the')
    dengan_spasi = teks.count('the ')

    print(f"{filename}:")
    print(f"  'the'  muncul {tanpa_spasi} kali")
    print(f"  'the ' muncul {dengan_spasi} kali")


for filename in ['teks_contoh.txt']:
    count_the(filename)
    