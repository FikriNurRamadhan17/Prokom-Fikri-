# Exercise 6.9
favorite_places = {
    'fikri': ['Bali', 'Bandung'],
    'budi': ['Yogyakarta'],
    'sari': ['Lombok', 'Raja Ampat', 'Bromo'],
}
for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        print(f"- {place}")