#6-1

person = {
    "first_name": "thelma",
    "last_name": "ponce",
    "age": 7,
    "city": "fontana"
}

print(person["first_name"].title())
print(person["last_name"].title())
print(person["age"])
print(person["city"].title())

#6-2 #6-10
favorite_numbers = {
    "samir": [7, 8, 14,13],
    "sagar": [15, 11, 6, 3, 9],
    "ashok": [10, 19, 21],
    "trent": [66, 56, 23],
    "alison": [1, 45, 44, 67]
}

for name, favorite_number in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")

    for number in favorite_number:
        print(f"\t{number}")
# print(f"Samir's favorite number is {favorite_numbers['samir']}") 
# print(f"Sagar's favorite number is {favorite_numbers['sagar']}")
# print(f"Ashok's favorite number is {favorite_numbers['ashok']}")
# print(f"Trent's favorite number is {favorite_numbers['trent']}")
# print(f"Alison's favorite number is {favorite_numbers['alison']}")

#6-3
glossary = {
    "dictionary": "A collection of key-value pairs.\n",
    "list": "List is a data structure used to store collection of data. Lists are ordered and mutuable.",
    "loop": "Loop is used to iterate through each value in a list.",
    "variables": "Variables store data values.",
    "Data Types": "Data types define the kind of data Python can handle.",
    "Conditional Statements": "Conditional statements make decisions in code.",
    "Functions": "Functions are reusable blocks of code."
}

for keys, values in glossary.items():
    print(f"{keys.title()}: {values}")

python_keyword = glossary.get("if_statements", "This keyword is not here.")
print(python_keyword)

glossary["if_statements"] = "A conditional statement that executes a block of code if a specified condition evaluates to true."
python_keyword = glossary.get("if_statements", "This keyword is not here.")
print(f"\nif_statements: {python_keyword}")

