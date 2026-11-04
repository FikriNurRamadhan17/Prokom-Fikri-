# Exercise 8.8
def make_album(artist, title, tracks=None):
    """Kembalikan dictionary berisi info album."""
    album = {'artist': artist, 'title': title}
    if tracks:
        album['tracks'] = tracks
    return album


while True:
    print("\n(Ketik 'q' kapan saja untuk keluar)")

    artist = input("Nama artis: ")
    if artist == 'q':
        break

    title = input("Judul album: ")
    if title == 'q':
        break

    album = make_album(artist, title)
    print(album)
    