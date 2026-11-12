def get_city_country(city, country, population=''):
    full = f"{city}, {country}"
    if population:
        full += f" – population {population}"
    return full.title()

