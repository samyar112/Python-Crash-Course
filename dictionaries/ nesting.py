alien_0 = {
    'color': 'green',
    'points': 5
    }

alien_1 = {
    'color': 'yellow',
    'points': 10
    }

alien_2 = {
    'color': 'red',
    'points': 15
    }

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

aliens = []

#Make 50 green aliens.

for alien_number in range(50):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:50]:
    print(alien)

print(f"Total number of aliens: {len(aliens)}")

