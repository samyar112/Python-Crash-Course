
#6-8

# # Create dictionaries representing different pets
# pet1 = {"kind": "dog", "owner": "Alice"}
# pet2 = {"kind": "cat", "owner": "Bob"}
# pet3 = {"kind": "parrot", "owner": "Charlie"}

# pets = [pet1, pet2, pet3]

# # for pet in pets:
# for keys, value in pet1.items():
#      print(keys, value)
# for keys, value in pet2.items():
#     print(keys, value)
# for keys, value in pet3.items():
#     print(keys, value)
    
#     # for kind_pet, pet_details in pets.items():
#         # print(f"Pet is : {pet_details}, Owner is: {pet_details}")
# Make an empty list to store the pets in.
pets = []

# Make individual pets, and store each one in the list.
pet = {
    'animal type': 'python',
    'name': 'john',
    'owner': 'guido',
    'weight': 43,
    'eats': 'bugs',
}
pets.append(pet)

pet = {
    'animal type': 'chicken',
    'name': 'clarence',
    'owner': 'tiffany',
    'weight': 2,
    'eats': 'seeds',
}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'peso',
    'owner': 'eric',
    'weight': 37,
    'eats': 'shoes',
}
pets.append(pet)

# Display information about each pet.
for pet in pets:
    print(f"\nHere's what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")
