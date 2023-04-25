#Moficiaciones archivos
#Agregar permisos a los archivos
#Permiso w+ hace que se sobrescriba todo el archivo
with open('./text.txt', 'r+') as file_2:
    # Leer todo el archivo
    print(file_2.read())
    file_2.write('\nAgregando cosas')
    print(file_2)