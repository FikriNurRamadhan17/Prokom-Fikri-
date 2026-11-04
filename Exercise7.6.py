# Exercise 7.6
# Versi 1: kondisi langsung di while
topping = ""
while topping != 'quit':
    topping = input("\nTopping (ketik 'quit' untuk selesai): ")
    if topping != 'quit':
        print(f"Oke, {topping} akan ditambahkan.")

# Versi 2: pakai variabel active (flag)
active = True
while active:
    topping = input("\nTopping (ketik 'quit' untuk selesai): ")
    if topping == 'quit':
        active = False
    else:
        print(f"Oke, {topping} akan ditambahkan.")

# Versi 3: pakai break
while True:
    topping = input("\nTopping (ketik 'quit' untuk selesai): ")
    if topping == 'quit':
        break
    print(f"Oke, {topping} akan ditambahkan.")