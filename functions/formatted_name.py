def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name("jimi", "hendrix")
musician1 = get_formatted_name("kurt", "cobain")
print(musician)
print(musician1)

#optional arguments add middle name

def get_formatted_name(first_name, last_name, middle_name = ""):
    """Return a full name, neatly formatted"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"

    return full_name.title()

musician2 = get_formatted_name("jimi", "hendrix", "lee")
musician3 = get_formatted_name("kurt", "cobain")

print(musician2)
print(musician3)