# Exercise 6.11
cities = {
    'jakarta': {
        'country': 'indonesia',
        'population': 10500000,
        'fact': 'ibu kota Indonesia',
    },
    'tokyo': {
        'country': 'japan',
        'population': 14000000,
        'fact': 'kota dengan area metropolitan terbesar di dunia',
    },
    'paris': {
        'country': 'france',
        'population': 2100000,
        'fact': 'rumah Menara Eiffel',
    },
}
for city, info in cities.items():
    print(f"\n{city.title()}")
    print(f"  Country: {info['country'].title()}")
    print(f"  Population: {info['population']}")
    print(f"  Fact: {info['fact']}")