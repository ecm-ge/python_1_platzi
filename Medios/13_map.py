#Funciones tranformadas

#Version Clasica
numbers = [1, 2, 3, 4, 5]
numbers_v2 = []

for i in numbers:
    numbers_v2.append(i*2)

print(numbers_v2)

#Version con MAP

numbers_v3 = list(map(lambda i: i*2, numbers))
print(numbers_v3)