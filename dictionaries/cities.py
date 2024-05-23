#6-11

cities = {
    'wichita': {
        'country': 'usa',
        'population': '396,192',
        'fact': 'Wichita is known as the "Air Capital of the World."'
    },

    'kathmandu': {
        'country': 'nepal',
        'population': '1,000,442',
        'fact': 'The city is one of the oldest continuously inhabited places in the world, founded in the 2nd century AD.'
    },

    'liverpool': {
        'country': 'england',
        'population': '496,784',
        'fact': "The city's football club is the best in the world."
    }
}

for city, city_infos in cities.items():
    print(f"\nHere's some information about the {city.title()} city:")

    for city_info, detail in city_infos.items():
        print(f"\t{city_info.title()}: {detail.title()}")

