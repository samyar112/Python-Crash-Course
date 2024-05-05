countries = ['Nepal', 'France', 'Mexico', 'China', 'England']

print(f"{countries[0]} is a beautiful country. I would love to travel there someday")
print(f"{countries[1]} is a beautiful country. I would love to travel there someday")
print(f"{countries[2]} is a beautiful country. I would love to travel there someday")
print(f"{countries[3]} is a beautiful country. I would love to travel there someday")
print(f"{countries[4]} is a beautiful country. I would love to travel there someday")

countries[0] = "USA"
print(f"I am currently in {countries[0]}.")

countries.append('India')
print(countries)

visited = countries.pop()
print(f"I've already visited to {visited}. I would not like to go there again.")

print(f"{countries[0]} is a beautiful country. I would love to travel there someday")
print(f"{countries[1]} is a beautiful country. I would love to travel there someday")
print(f"{countries[2]} is a beautiful country. I would love to travel there someday")
print(f"{countries[3]} is a beautiful country. I would love to travel there someday")
print(f"{countries[4]} is a beautiful country. I would love to travel there someday")

countries.insert(3, 'Japan')
print(f"I want to go to {countries[3]}.")

order_of_countries = sorted(countries)
print(order_of_countries)
print(f"I would like to visit countries in this order: {order_of_countries}")
print(len(countries))
reverse_order = sorted(countries, reverse = True)
print(f"Nevermind! I would like to visit all these places in this order: {reverse_order}")

del countries[-1]
del countries[-1]
del countries[-1]
del countries[-1]
del countries[-1]
del countries[-1]


print(f"I have visited all the listed countries: I don't have a list now. It's empty {countries}.")