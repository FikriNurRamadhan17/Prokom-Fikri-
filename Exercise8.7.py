# Exercise 8.7
def make_album(artist, title, tracks=None):
    """Kembalikan dictionary berisi info album."""
    album = {'artist': artist, 'title': title}
    if tracks:
        album['tracks'] = tracks
    return album


print(make_album('Coldplay', 'Parachutes'))
print(make_album('Adele', '21'))
print(make_album('Dewa 19', 'Pandawa Lima'))
print(make_album('Taylor Swift', '1989', tracks=13))
