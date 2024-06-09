#7-8
sandwich_orders = ['spicy chicken sandwich','baconator sandwich', 'famous star sandwich']

finished_sandwiches =  []

while sandwich_orders:
    current_orders = sandwich_orders.pop()
    print(f"I made your {current_orders}")
    finished_sandwiches.append(current_orders)

print(f"Here is the list of your confirmed orders of sandwiches:")
for finished_sandwich in finished_sandwiches:
    print(f"{finished_sandwich.title()}")

