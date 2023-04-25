#Strings y sus comportamientos

name = 'Eric'
last_name = 'Contreras'

#Formas de concatenar

full_name = name + ' ' + last_name
print(full_name)

template = "Mi nombre es " + name + " y mi apellido es " + last_name
print(template)

template = "Hola mi nombre es {} y mi apellido es {}".format(name, last_name)
print(template)

template = f"Hey! mi nombre es {name} y mi apellido es {last_name}"
print(template)