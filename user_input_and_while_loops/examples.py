#1.
name = input("Please enter your name: ")
print(f"\nHello, {name.title()}!")

#2.
prompt = "I need your name to start the program."
prompt += "\n What's your name? "

name = input(prompt) 
print(f"Great to have you here, {name.title()}!")

#3.
age = input("How old are you? ")
# input always returns string. Need to change it to int first.
age = int(age)

if age >= 21:
    print("Welcome to the bar! Which cocktail would like to drink?")
else:
    print("You are not allowed to drink alcohol.")

#4. % Modular operators, Divides one number with anothe and returns remainder.
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\n The number {number} is even.")
else:
    print(f"\n The number {number} is odd.")

