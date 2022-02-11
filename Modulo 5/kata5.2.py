from math import dist


planet_one=input("Planeta 1: ")
planet_two=input("planeta 2: ")

distance = abs(int(planet_one)- int(planet_two))
distancef = distance *.0621

print(distance)
print(round(distancef))
