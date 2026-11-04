# Exercise 8.5
def describe_city(city, country='Indonesia'):
    """Tampilkan kota dan negaranya."""
    print(f"{city.title()} is in {country.title()}.")


describe_city('surakarta')
describe_city('jakarta')
describe_city('tokyo', 'japan')
