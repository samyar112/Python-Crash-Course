#5-10
current_users = ["Charles", "Caroline", "Laura", "Mary", "Carrie", "Albert", "Grace", "Alfanzo"]

new_users = ["Laura", "Hanson", "Edwards", "Laura", "Mary", "Alfanzo"]

lowercase_current_users = [current_user.lower() for current_user in current_users]
print(lowercase_current_users)

lowercase_new_users = [new_user.lower() for new_user in new_users]
print(lowercase_new_users)

#first loop through the lowercase new users. Then, check to see if new users are in the current list. 
for new_user in lowercase_new_users:
    if new_user in lowercase_current_users: 
        print(new_user)
        print("Username is already taken. Choose another username.\n")
        
    else: 
        print(new_user)
        print("Username is available.\n")