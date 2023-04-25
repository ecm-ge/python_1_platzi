#Multiples retornos y valores por defecto

def volumen (altura=1, ancho=1, prof=1):
    return altura*ancho*prof

print(volumen(1,2,3))
print(volumen(ancho=2))
print(volumen())

#Retornar una tupla de valoresS

def volumen_2 (altura=1, ancho=1, prof=1):
    return altura*ancho*prof, ancho, 'XD'

print(volumen_2())