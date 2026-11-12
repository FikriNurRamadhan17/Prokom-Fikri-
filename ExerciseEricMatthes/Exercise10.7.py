# Exercise 10-7
print("Kalkulator penjumlahan. Ketik 'q' kapan saja untuk keluar.")

while True:
    first = input("\nAngka pertama: ")
    if first == 'q':
        break

    second = input("Angka kedua: ")
    if second == 'q':
        break

    try:
        total = int(first) + int(second)
    except ValueError:
        print("Maaf, yang kamu masukkan bukan angka. Coba lagi.")
    else:
        print(f"Hasilnya: {total}")
        
        
        