# Exercise 8.3
def make_shirt(size, text):
    """Tampilkan ukuran dan tulisan pada kaos."""
    print(f"Kaos ukuran {size} dengan tulisan '{text}'.")


# Positional argument (urutan harus sesuai)
make_shirt('M', 'I love Python')

# Keyword argument (urutan bebas, nama harus sama dengan parameter)
make_shirt(text='Teknik Industri UNS', size='L')
