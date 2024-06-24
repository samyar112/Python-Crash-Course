#8.6
def city_country(city, country):
    print(f"{city.title()}, {country.title()}")

city_country("santiago", "chile")
city_country("kathmandu", "nepa;")
city_country("mexico city", "mexico")

#8.7
musician = []
def make_album(artist, album_title, number_of_songs = None):
    songs = {'artist': artist, 'album': album_title, 'number_of_songs': number_of_songs}
    return songs

musician0 = make_album("Pearl Jam", "Ten")
musician.append(musician0)

musician1 = make_album("Linkin Park", "A thousand suns")
musician.append(musician1)

musician2 = make_album("Mariah Carey", "Butterfly")
musician.append(musician2)

musician3 = make_album("Greenday", "Dookie", 10)
musician.append(musician3)


print(musician)

#8.8 User Albums
while True: 
    artist = input("Artist Name: ")
    if artist == 'q':
        break
    album = input("Album Name: ")
    if album == 'q':
        break
    songs = input("How many songs are there? ")
    if songs == 'q':
        break
    make_album(artist, album, songs) 

