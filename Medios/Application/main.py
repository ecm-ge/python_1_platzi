import mod

keys, values = mod.get_population()

print(keys)
print(values)

data = [
    {
        'country':'Colombia',
        'population':500
    },
    {
        'country': 'Bolivia',
        'population': 300
    }
]
country = input('Ingrese el pais: ')

result = mod.population_by_country(data, country)
print(result)