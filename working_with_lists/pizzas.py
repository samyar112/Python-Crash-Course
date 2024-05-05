#Exercise 4-1
pizza_types = ['Margherita', 'Pepperoni', 'Hawaiian', 'Vegetarian', 'Meat Lover']
for pizza in pizza_types:
    print(f"I like {pizza}. I am going to eat it this weekend with my wife.")

print("\nI really love pizza! But I love my wife more.")

#4-11
friend_pizzas = pizza_types[:]
friend_pizzas.append('Chicken')
print("\nMy favorite pizzas are:")


for pizza in pizza_types:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
