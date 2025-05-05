from math import pi
from random import choice as ch

planets = [
  'Mercury',
  'Venus',
  'Earth',
  'Mars',
  'Saturn'
]

randomPlanet = ch(planets)

r = 0

if randomPlanet == "Mercury":
    r = 2440
elif randomPlanet == "Venus":
    r = 6052
elif randomPlanet == "Earth":
    r = 6371
elif randomPlanet == "Mars":
    r = 3390
elif randomPlanet == "Saturn":
    r = 58232
else:
    print("Error.")

area = 4 * pi * r ** 2

print(f"The surface area of {randomPlanet} is {round(area, 2)}")