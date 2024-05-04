#Exercise 3-4
guests = ['Sagar', 'Ashok', 'Bijay']
message = "I would like to invite you to the dinner party. I hope you can make it."


print(f"Hi {guests[0].upper()}, {message}")
print(f"Hi {guests[-2].upper()}, {message}")
print(f"Hi {guests[-1].upper()}, {message}")

#Exercise 3-5
print(guests[0])
guests[0] = 'Rohit'

print(f"Hi {guests[0].upper()}, {message}")
print(f"Hi {guests[-2].upper()}, {message}")
print(f"Hi {guests[-1].upper()}, {message}")

#Exercise 3-6

print(f"{guests[0]}, I have found a bigger dinner table.")
print(f"{guests[1]}, I have found a bigger dinner table.")
print(f"{guests[2]}, I have found a bigger dinner table.")

guests.insert(0, 'Shirish')
print(guests)

guests.insert(2, 'Sujan')
print(guests)

guests.insert(3, 'Sanjay')

guests.append('Yaman')
print(guests)

#Exercise 3-7

print("Sorry guys, I only have space for two people.")

#Exercise 
print(len(guests))

print(guests)
friend = guests.pop()
print(guests)
print(f"Sorry! {friend} I can't invite you to dinner this time.")
friend = guests.pop()
print(f"Sorry! {friend} I can't invite you to dinner this time.")
friend = guests.pop()
print(f"Sorry! {friend} I can't invite you to dinner this time.")
friend = guests.pop()
print(f"Sorry! {friend} I can't invite you to dinner this time.")
friend = guests.pop()
print(f"Sorry! {friend} I can't invite you to dinner this time.")

print(guests)

message = "you are still invited."
print(f"{guests[0]}, {message}")
print(f"{guests[1]}, {message}")

del guests[0]
print(guests)

del guests [0]
print(guests)
