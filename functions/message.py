#8.1
def display_message():
    print("We will be learning how to call function")

display_message()

#8.2
def favorite_book(title):
    print(f"One of my favorite books is {title}")

title = "Alice in Wonderland"

favorite_book(title)
#parameter
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"\nMy {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"\nMy {animal_type}'s name is {pet_name.title()}.")
#calling argument explicitly, order don't matter
describe_pet(pet_name = 'harry', animal_type = 'hamster')

#default key value for parameter.
def describe_pet(animal_type, pet_name = "chato"):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"\nMy {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type = 'cat')
#an explicit argument for pet_name, default value will be ignored.
describe_pet(pet_name = 'harry', animal_type = 'cat')



