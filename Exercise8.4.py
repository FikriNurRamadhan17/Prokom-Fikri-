# Exercise 8.4
def make_shirt(size='large', text='I love Python'):
    """Tampilkan ukuran dan tulisan pada kaos."""
    print(f"Kaos ukuran {size} dengan tulisan '{text}'.")


make_shirt()                                  # large, tulisan default
make_shirt(size='medium')                     # medium, tulisan default
make_shirt('small', 'Semangat kuliah!')       # tulisan berbeda
