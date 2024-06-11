#8.3
def make_shirt(size, text):
    print(f"Size: {size}")
    print(f"{text}")

make_shirt("large", "You're worth it!")
make_shirt(size = "large", text = "You're worth it!")


#8-4
def make_shirt(message = "I love Python", size = "large"):
    print(f"Size: {size}")
    print(f"{message}")

make_shirt()
make_shirt(size = "medium")
make_shirt(message = "I love visual studio.")

#8-5
def describe_city(city, country = "Nepal"):
    print(f"{city.title()} is in {country.title()} ")

describe_city("Kathmandu")
describe_city(city = "Pokhara")
describe_city(city = "New Delhi", country = "India") 

