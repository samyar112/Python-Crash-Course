car = "Toyota"
print(f"{car == 'subaru'}? I predited False.")

requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print("cheese" in requested_toppings)

requested_toppings.append('cheese')
print("cheese" in requested_toppings)

dortmund_score = 1
psg_score = 2

if dortmund_score > psg_score:
    print("Dortmund goes to the final!")
elif dortmund_score == psg_score:
    print("Game decided by the penalty!")
else:
    print("PSG goes to the final.")

banned_users = ['jordan', 'Brandt', 'reus', 'sanchO']

banned_user = []

for user in banned_users:
    user_1 = user.lower()
    banned_user.append(user_1)

print(banned_user)

user = "sancho"

if user not in banned_user:
    print(f"{user.title()} can enter the building.")
else:
    print("You are banned!")

champions_finalist_1 = "Bayern Munich"
champions_finalist_2 = "Real Madrid"
winner = champions_finalist_2

print(champions_finalist_1 == winner) 
print (champions_finalist_2 == winner)

# or & and conditions

age_0 = 2
age_1 = 18

print((age_0 >= 1) or (age_1 <= 17))
print((age_0 >= 1) and (age_1 <= 17))

#if, elif, else, input, and function: 

def admission_fee(age: int): 
    if age < 4:
        print("Free Admission")
    elif age <= 18:
        print("Admission fee is $25")
    else:
        print("Admission fee is $40")

age = int(input("What's your age? "))

admission_fee(age)