#7-3

user = "Provide me a number, and I'll tell you if the number is a multiple of 10 or not.\n"
user += "What's the number? "
number = input(user)
number = int(number)

if number % 10 == 0: 
    print(f"Yes, {number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")

