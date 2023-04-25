#Dictionary Comprenhension

dict = {}

for i in range (1,11):
    dict[i]= i*2

print(dict)

#Segunda forma

dict_v2 = { i: i*2 for i in range (1,11) }
print(dict_v2)

#Otro uso

names = ['nico', 'santi', 'zule']
ages = [12, 56, 98]

personas = {names[i]:ages[i] for i in range(len(names)) }
print(personas)