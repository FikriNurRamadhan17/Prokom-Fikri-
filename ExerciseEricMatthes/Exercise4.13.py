# Exercise 4.13
foods = ('nasi goreng', 'mie ayam', 'bakso', 'sate', 'soto')
for food in foods:
    print(food)

# foods[0] = 'rendang'   # ini error: tuple tidak bisa diubah

foods = ('rendang', 'mie ayam', 'bakso', 'gado-gado', 'soto')
print("\nMenu baru:")
for food in foods:
    print(food)
    