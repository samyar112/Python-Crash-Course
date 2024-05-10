#5-8

admins = ["Sagar", "Ashok", "Bijay", "Rohit"]

username = "Ashok"

if username in admins:
        print(f"Hello {username}, would you like to see a status report?")
else:
     print(f"Hello {username} , thank you for logging again.")

#5-9
del admins[:]
print(admins)

if len(admins) == 0: 
    print("We need to find some users!")


