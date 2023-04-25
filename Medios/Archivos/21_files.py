#Lectura de archivos

file = open('./text.txt')

#Leer linea por linea
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())

file.close()
print('-------------------------')

#Cerrar sin el close
with open('./text.txt') as file_2:
    # Leer todo el archivo
    print(file_2.read())
