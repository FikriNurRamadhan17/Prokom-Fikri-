# Exercise 10-6
print("Masukkan dua angka, nanti aku jumlahkan.")

first = input("Angka pertama: ")
second = input("Angka kedua: ")

try:
    total = int(first) + int(second)
except ValueError:
    print("Maaf, yang kamu masukkan bukan angka.")
else:
    print(f"Hasilnya: {total}")
    