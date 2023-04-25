#CRUD: Create Read Update Delete

numbers = [1, 2, 3, 4, 5]
other_numbers = ['Uno', 'Dos', True]
print(numbers[1])

#Metodos para agregar

#FIinal lista
numbers.append(6)
print(numbers)

#Elegir posicion/ (Posicion, Elemento)
numbers.insert(0, 0)
print(numbers)

#Unir Listas
new_list = numbers + other_numbers
print(new_list)

#Buscar elemento en lista
print(new_list.index('Dos'))

#Eliminar elementos, por nombre
new_list.remove('Uno')
print(new_list)

#Eliminar ultimo elemento
new_list.pop()
print(new_list)

#O por posicion
new_list.pop(0)
print(new_list)

#Colocar lista alreves
numbers.reverse()
print(numbers)

#Ordenar lista
numbers.sort()
print(numbers)