#Operaciones entre conjuntos

set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}
set_x = {'xd'}

#Union de conjuntos
set_c = set_a.union(set_b,set_x)
print(set_c)

#Interseccion de conjuntos
set_c = set_a.intersection(set_b)
print(set_c)

#Diferencia de conjuntos
set_c = set_a.difference(set_b)
print(set_c)

#Diferencia Simetrica
set_c = set_a.symmetric_difference(set_b)
print(set_c)