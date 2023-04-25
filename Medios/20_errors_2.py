#Manejo de errores
try:
    print(0/0)
except ZeroDivisionError as error:
    print(error)

#Segundo manejo acumulativo
try:
    print(0 / 0)
    age=10
    if age < 18:
        raise Exception('Ola k ase')
except ZeroDivisionError as error:
    print(error)
except Exception as error:
    print(error)