users = {
    'spandey': {
        'first': ' samir',
        'last': 'pandey',
        'location': 'kathmandu',
    },

    'tponce': {
        'first': 'thelma',
        'last': 'ponce',
        'location': 'fontana'
    }
}

for username, user in users.items(): 
    print(f"Username: {username}")
    print(f"    Full name: {user['first'].title()} {user['last'].title()}")
    print(f"    Location: {user['location'].title()}\n")





# Username: aeinstein
#     Full name: Albert Einstein
#     Location: Princeton”
