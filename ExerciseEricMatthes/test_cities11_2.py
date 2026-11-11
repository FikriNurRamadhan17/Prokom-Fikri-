from city_functions11_2 import get_city_country

def test_city_country():
    result = get_city_country('santiago', 'chile')
    assert result == 'Santiago, Chile'

def test_city_country_population():
    result = get_city_country('santiago', 'chile', population=5000000)
    assert result == 'Santiago, Chile – Population 5000000'