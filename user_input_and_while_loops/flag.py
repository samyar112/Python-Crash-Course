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

