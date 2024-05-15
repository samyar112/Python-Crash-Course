#6-5

rivers = {
    'amazon': 'brazil',
    'nile': 'egypt',
    'yangtze': 'china'
}

for key, value in rivers.items():
    print(f"The {key.title()} runs through {value.title()}.")

for key in rivers.keys():
    print(f"The {key.title()}")

for value in rivers.values():
    print(f"{value.upper()}")