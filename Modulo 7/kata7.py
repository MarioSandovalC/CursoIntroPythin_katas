from time import sleep

planets = []
new_planet = ''

while new_planet != 'done':
    if new_planet:
        planets.append(new_planet)
    new_planet= input('Write the name of a planet, when you finishes type done: ')

sleep(1)

for planet in planets:
    print(planet)
    sleep(1)
    
