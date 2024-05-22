#6-9
favorite_places = {
    'sagar': ['pokhara', 'kathmandu', 'banepa'],
    'samir': ['fontana', 'alaska', 'mexico city'],
    'mayalu': ['alaska', 'colorado', 'new york', 'wichita']
}

for friend, favorite_place in favorite_places.items():
    print(f"\n{friend.title()}'s favorite place is:")
    for place in favorite_place:
        print(f"    {place.title()}")