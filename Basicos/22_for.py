#Ciclo repetitivo un numero X de veces

#Declarar numero de veces que se repite

for element in range(1, 20):
    print(element)

print('------------------')

#Recorrer elementos

lista = [1, 2, 3, 4, 5]

for e in lista:
    print(e)

print('------------------')

tupla = (1, 2, 3, 4, 5)

for e in tupla:
    print(e)

print('------------------')

producto={
    'name': 'Carne',
    'price': 2000,
    'stock': True
}

for e in producto:
    print(producto[e])