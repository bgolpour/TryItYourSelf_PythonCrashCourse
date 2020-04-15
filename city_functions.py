def city_functions(city, country, population=''):
    if population:
        city_name = city + ' ' + country + ' ' + population
    else:
        city_name = city + ' ' + country
    return city_name.title()

