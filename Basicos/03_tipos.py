#Tipos de datos

#String: Cadena de texto, siempre se debe poner en "" o ''
my_name = "Eric"

#Funcion que me dira el tipo de la variable
print(type(my_name))

#Int: Numeros
my_age = 28
print(type(my_age))

#Bool: Tiene valor posible True o False nada mas
is_single = True
print(type(is_single))

#Cuando pedimos por consola siempre sera un str para transformar debemos colocar la funcion antes del input
is_number = input('Digite lo que quiera: ')
print(type(is_number))

is_number = int(input('Digite lo que quiera: '))
print(type(is_number))