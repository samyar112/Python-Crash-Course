#6-7
people = {
    "person1": { 
    "first_name": "thelma",
    "last_name": "ponce",
    "age": "24",
    "city": "mexico city"
    },

    "person2": { 
    "first_name": "sagar",
    "last_name": "maharjan",
    "age": "17",
    "city": "fontana"
    },

    "person3": { 
    "first_name": "shirish",
    "last_name": "sharma",
    "age": "18",
    "city": "dehli"
    },
}

for person_key, person_details in people.items():
    print(f'Name: {person_details["first_name"].title()} {person_details["last_name"].title()}')
    print(f'Age: {person_details["age"]}')
    print(f'City: {person_details["city"].title()}\n')