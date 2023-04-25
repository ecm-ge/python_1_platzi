#Cadenas

#Encontrar texto dentro de una cadena de texto
text = 'Yo se mucho de BBDD'
a = 'mucho' in text
print(a)
print('--------------')

#Tamaño de una cadema
tam = len(text)
print(tam)
print('--------------')

#Colocar en mayusculas o minusculas el texto
print(text.upper())
print(text.lower())
print('--------------')

#Contar cuantas veces aparece algo
print(text.count('se'))
print('--------------')

#Invertir Mayus y Mins
print(text.swapcase())
print('--------------')

#Consulta si el texto inicia o finaliza con algo
print(text.startswith('Yo'))
print(text.endswith('BBDD'))
print('--------------')

#Cambia algo en la cadena por otra cosa
print(text.replace('BBDD', 'Python'))
print('--------------')