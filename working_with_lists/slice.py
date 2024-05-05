#slice

players = ["Trent", "Robertson", "Salah", "Coutinho", "Agger", "Konate"]
# print players from Salah to Konate
print(players[2:])
print(players[-4:])

#print players from Robertson to Agger
print(players[1:5])

#print players from Trent to Salah
print(players[0:3])
print(players[:3])

players.append("Gerrard")
#print players from Trent to Gerrard but skip two players after selecting one
print(players[0:7:3])

for value in range(2,31,2):
    print (value/2)

values = [value for value in range(1,31)]
print(values)

lfc_players = players[:]
print(lfc_players)
lfc_players.append("Torres")
print(lfc_players)
print(players)