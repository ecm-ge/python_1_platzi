#Son listas pero no son modificables

numbers = (1, 2, 3, 4, 2)
print(numbers)

strings = ('XD', 'XP', 'X3')
print(type(strings))

#Buscar elemento en la tupla
print(numbers.index(3))

#Contar elemento en tupla
print(numbers.count(2))

#Agregar elementos de una tupla a una lista
my_list = list(strings)
print(my_list)
print(type(my_list))

#Convertir una lista a tupla
my_list.append('OuO')
print(my_list)
strings = tuple(my_list)
print(strings)
print(type(strings))S