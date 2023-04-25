#Alcance Scope

#Variable Global
price= 100

def incrementar():
    result=200 #Variable Local
    result+=10
    return result

print(price)

price = incrementar()
print(price)