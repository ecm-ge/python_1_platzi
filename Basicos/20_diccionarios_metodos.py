#Declaracion

persona = {
    'nombre': 'Eric',
    'apellido': 'Contreras',
    'edad': 28,
    'lenguajes': ['python, SQL, C++']
}

print(persona)

#Modificar datos
persona['nombre'] = 'Eric Yair'

#Al ser lista podemos agregar asi
persona['lenguajes'].append('Java')
print(persona)

#Eliminar llaves con valor
del persona['apellido']
print(persona)
persona.pop('edad')
print(persona)

#Agregar datos
persona['apellido'] = 'Contreras Muñoz'
persona['edad'] = 28

#Obtener datos
print(persona.items())
print(persona.keys())
print(persona.values())