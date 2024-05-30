prompt = "\n Tell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program: "

active = True
while active:
    message = input(prompt).lower()
    if message == 'quit':
        active = False
    else: 
        print(message)
print("Program closed.")
        
#input return in CAPS and quit in case insensitive.
interaction_message = "\n Type something, and I'll repeat it: "
interaction_message+= "Enter 'quit' to end: "
quit_program = 'quit'

active = True

while active:
    message = input(interaction_message)
    if message.lower() == quit_program:
        acitve = False
    else:
        print(message.upper())

#while loop break and continue

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True: 
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")

#continue loop

current_number = 0
while current_number <10:
    current_number += 1 
    if current_number % 2 == 0:
        continue
    print(current_number)


#infinite loop

x = 1
while x <= 5:
    print(x)
    x += 1 