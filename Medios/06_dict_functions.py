#Funciones

import random

countries = ['col', 'mex', 'bol', 'pe']

population = { c: random.randint(1,100) for c in countries}
print(population)

result = { c: population for (c, population) in population.items() if population > 20 }
print(result)