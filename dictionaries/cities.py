#6-11

cities = {
    'wichita': {
        'country': 'USA',
        'population': 396_192,
        'fact': 'Wichita is known as the "Air Capital of the World."'
    },

    'kathmandu': {
        'country': 'Nepal',
        'population': 1_000_442,
        'fact': 'The city is one of the oldest continuously inhabited places in the world, founded in the 2nd century AD.'
    },

    'liverpool': {
        'country': 'England',
        'population': 496_784,
        'fact': "The city's football club is the best in the world."
    }
}

for city, city_infos in cities.items():
    print(f"\nHere's some information about the {city.title()} city:")
    
    country = f"{city_infos['country']}"
    population = "{:,}".format(city_infos['population'])
    fact = f"{city_infos['fact']}"

    print(f"Country: {country}") 
    print(f"Population: {population}")
    print(f"Fact: {fact}")
# another way...
    for city_info, detail in city_infos.items():
        print(f"\t{city_info.title()}: {detail}")

