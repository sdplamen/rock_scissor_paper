#G's relative to earth

Sunweight = 28.02
Mercuryweight = 0.377
Venusweight = 0.904
Moonweight = 0.165
Marsweight = 0.379
Jupiterweight = 2.53
Saturnweight = 1.065
Uranusweight = 0.89
Neptuneweight = 1.14
Plutoweight = 0.063

weight = None
planets = {
    "Sun": Sunweight,
    "Mercury": Mercuryweight,
    "Venus": Venusweight,
    "Moon": Moonweight,
    "Mars": Marsweight,
    "Jupiter": Jupiterweight,
    "Saturn": Saturnweight,
    "Uranus": Uranusweight,
    "Neptune": Neptuneweight,
    "Pluto": Plutoweight
}

weight = float(input("Whats your weight on earth?(in kg):"))
for planet in planets:
    print(f'Your weight on {planet} is {weight * planets[planet]} kg')
