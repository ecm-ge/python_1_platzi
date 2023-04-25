#Funciones dentro de otras funciones

def incrementar (x):
    return x+1

def hof (x, func):
    return x + func(x)

result = hof(2, incrementar)
print(result)