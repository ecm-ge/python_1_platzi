#Operadores de comparacion AND cuando quiero ambas condiciones se cumplan

#AND
print(True and True)
print(True and False)
print(False and True)
print(False and False)

stock = int(input("Digite el stock: "))

print(stock > 100 and stock <= 1000)

#OR
print(True or True)
print(True or False)
print(False or True)
print(False or False)

stock = str(input("Digite el rol: "))

print(stock == 'admin' or stock == 'seller')