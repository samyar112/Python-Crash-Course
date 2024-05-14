user_0 = {
    'username': 'spandey',
    'first': 'samir',
    'last': 'pandey'
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
#looping through key and value pair.
for key, value in favorite_languages.items():
  print(f"{key.title()} knows how to code in {value} language.\n")

#looping through just the keys
for name in favorite_languages.keys():
   print(f"{name.title()}")

friends = ['phil', 'sarah']

for name in favorite_languages.keys():
    print(f"{name.title()}")
    if name in friends:
      language = favorite_languages[name].title()
      print(f"{name.title()}, I see you love {language}!")
   
#looping through a dictionary's key by sorting.
poll_takers = ['phil', 'sarah'] 
for name in sorted(favorite_languages.keys()):
   if name in poll_takers:
      print(f"{name.title()}, thank you for taking the poll.")
   else:
      print(f"{name.title()}, please don't forget to take the poll.")
#    print(f"\n{name.title()}, thank you for taking the poll.")
   
