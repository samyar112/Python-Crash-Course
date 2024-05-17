#Store information about a pizza being ordered

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}

#Summarize the order
print(f"You ordered a {pizza['crust']} crust pizza with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")


favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python'],
}

for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print(f"\n{name.title()} likes the following programming language are:")
    else:
        print(f"\n {name.title()}'s favorite language is: ")

    for language in languages:
        print(f"\t{language.upper()}")
