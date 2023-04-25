#Operaciones con conjuntos/sets

set_countries = {'col', 'mex', 'fra'}

#Tamaño
size = len(set_countries)
print(size)

#Averiguar datos
print('col' in set_countries)
print('pe' in set_countries)

#Agregar data
set_countries.add('pe')
print(set_countries)

#Agregar mayor cantidad de elementos
set_countries.update({'ar', 'ec', 'pe'})
print(set_countries)

#Eliminar elementos / Tira error si no esta
set_countries.remove('ec')
print(set_countries)

#Eliminar elementos / NO tira eeror si no esta
set_countries.discard('pe')
print(set_countries)

#Vaciar todo
set_countries.clear()
print(set_countries)