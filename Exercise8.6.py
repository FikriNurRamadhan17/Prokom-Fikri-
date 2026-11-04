# Exercise 8.6
def city_country(city, country):
    """Kembalikan kota dan negara dalam satu string."""
    return f"{city.title()}, {country.title()}"


print(city_country('santiago', 'chile'))
print(city_country('surakarta', 'indonesia'))
print(city_country('paris', 'france'))

