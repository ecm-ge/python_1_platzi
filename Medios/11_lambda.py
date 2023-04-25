#Funciones Lambda

def incrementar (x):
    return x+1

result = incrementar(8)
print(result)

#Asi se hacen

incrementar_v2 = lambda x: x+1
result_v2 = incrementar_v2(9)
print(result_v2)