from city_functions11_1 import get_city_country

def test_city_country():
    result = get_city_country('santiago', 'chile')
    assert result == 'Santiago, Chile'