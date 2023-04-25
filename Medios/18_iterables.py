#Ciclo normal

for i in range (1,11):
    print(i)

#Nueva version - Se maneja manual / Al llegar al limite se lanza una exepcion

my_iter = iter(range(1,11))
print(my_iter)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))