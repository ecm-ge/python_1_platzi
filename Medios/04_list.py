#Mas listas

#Primera forma
numbers = []

for e in range (1,11):
    numbers.append(e*2)

print(numbers)

#Segunda forma List Comprenhension
numbers_v2 = [element*2 for element in range(1,11)]
print(numbers_v2)

#Condicional al ciclo
numbers_v3 = [element*2 for element in range(1,11) if element%2==0]
print(numbers_v3)