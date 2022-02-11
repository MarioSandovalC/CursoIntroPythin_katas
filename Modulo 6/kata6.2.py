# Lista de planetas
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Neptune']

search = input("Type the name of the planet(the first letter in Caps please): ")

place = planets.index(search)
print("The planet", planets[place], "is the number ",place+1)

close=planets[0:place]
print("Planets closest to the Sun", close)

far=planets[place+1:8]
print("Planets furthest from the Sun", far)