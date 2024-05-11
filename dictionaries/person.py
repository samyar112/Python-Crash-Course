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

#6-2
favorite_numbers = {
    "samir": 7,
    "sagar": 15,
    "ashok": 10,
    "trent": 66,
    "alison": 1
}

print(f"Samir's favorite number is {favorite_numbers['samir']}") 
print(f"Sagar's favorite number is {favorite_numbers['sagar']}")
print(f"Ashok's favorite number is {favorite_numbers['ashok']}")
print(f"Trent's favorite number is {favorite_numbers['trent']}")
print(f"Alison's favorite number is {favorite_numbers['alison']}")

#6-3
glossary = {
    "dictionary": "A collection of key-value pairs.\n",
    "list": "List is a data structure used to store collection of data. Lists are ordered and mutuable.\n",
    "loop": "Loop is used to iterate through each value in a list."
}

print(f"Dictionary: {glossary['dictionary']}\n")
print(f"List: {glossary['list']}\n")
print(f"Loop: {glossary['loop']}\n")

python_keyword = glossary.get("if_statements", "This keyword is not here.")
print(python_keyword)

glossary["if_statements"] = "A conditional statement that executes a block of code if a specified condition evaluates to true."
python_keyword = glossary.get("if_statements", "This keyword is not here.")
print(f"\nif_statements: {python_keyword}")

