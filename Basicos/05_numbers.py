#Datos de tipo numerico

#Enteros
lives = 3
print(type(lives))

#Flotantes
temperature = 12.5
print(type(temperature))

#Incrementales y decrementales
numero = 5
#Decremento
numero -= 1
print(numero)
#Incremento
numero += 2
print(numero)

#Challenge
var_1 = int(input("Diga el presupuesto del 1er mes: "))
var_2 = int(input("Diga el presupuesto del 2do mes: "))
var_3 = int(input("Diga el presupuesto del 3er mes: "))

var_4 = (var_1+var_2+var_3)/3

print("El promedio del presupuesto es de {}".format(var_4))