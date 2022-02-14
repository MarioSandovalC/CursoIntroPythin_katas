moons = 0
planets = 0
total_moons = 0
planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}
moons= planet_moons.values()
print(moons)
planets = len(planet_moons.keys())
print(planets)

for values in planet_moons.values():
    total_moons = total_moons + values

average = total_moons / planets

print(average)