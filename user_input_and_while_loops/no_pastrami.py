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