#7-9
sandwich_orders = ['pastrami', 'spicy chicken sandwich', 'pastrami', 'beef sandwich', 'pastrami', 'tuna sandwich']

finished_sandwiches =  []

print("We are out of Pastrami Sandwiches")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_orders = sandwich_orders.pop()
    print(f"I made your {current_orders}")
    finished_sandwiches.append(current_orders)

print(f"Here is the list of your confirmed orders of sandwiches:")
for finished_sandwich in finished_sandwiches:
    print(f"{finished_sandwich.title()}")

#7-10
poll_result = {}
polling_active = True
while polling_active:
    name = input("What's your name? ")
    dream_vacation = input("If you could visit one place in the world,\n where would you go? ")

    poll_result[name] = dream_vacation
    repeat = input("Would you like to let another person respond?(yes/no) ")

    if repeat =='no':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in poll_result.items():
    print(f"{name.title()} has a dream to visit {response} someday.")