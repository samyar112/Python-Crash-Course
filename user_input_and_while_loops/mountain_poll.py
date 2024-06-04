responses = {}

#set a flag to indicate that polling is active
polling_active = True

while polling_active:
    name = input("\n What is your name?")
    response = input("Which mountain you like to climb someday?")

    #Store the response in the dictionary.
    response[name] = response

    #Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no)")
    if repeat == 'no':
        polling_active = False

    #Polling is complete. Show the results.
    print("\n-- Poll Results--")
    for name, response in responses.items():
        print(f"{name} would like to climb {response}.")