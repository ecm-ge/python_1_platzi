#Comparativa de flotantes
x = 3.3
y = 1.1+2.2
print("x: {} Y: {}".format(x,y))

#Elegir los decimales a mostrar

y_str = format(y, ".2g")
print(y_str)

#Con tolerancia

tol = 0.00001
print(abs(x-y)<tol)