# Exercise 3.7
guests = ['Messi', 'Neymar', 'Ronaldo',
          'Mbappe', 'Halland', 'Dembele']
print("Maaf, saya hanya bisa mengundang dua orang.")

dikeluarkan = guests.pop()
print(f"Maaf {dikeluarkan}, saya tidak bisa mengundang Anda.")
dikeluarkan = guests.pop()
print(f"Maaf {dikeluarkan}, saya tidak bisa mengundang Anda.")
dikeluarkan = guests.pop()
print(f"Maaf {dikeluarkan}, saya tidak bisa mengundang Anda.")
dikeluarkan = guests.pop()
print(f"Maaf {dikeluarkan}, saya tidak bisa mengundang Anda.")

print(f"Halo {guests[0]}, Anda masih diundang.")
print(f"Halo {guests[1]}, Anda masih diundang.")

del guests[0]
del guests[0]
print(guests)
