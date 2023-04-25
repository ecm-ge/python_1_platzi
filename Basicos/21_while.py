#Ciclos, instrucciones repetitivas.

#Ciclo clasico

counter = 0
while counter < 10:
    counter+=1
    print('XD {}'.format(counter))

print('-----------------')
#Romper el ciclo antes de tiempo

counter_2 = 0
while counter_2 < 20:
    counter_2+=1
    if counter_2 == 15:
        break
    print(counter_2)

print('-----------------')

#Saltar a la siguiente instruccion omitiendo la directa

counter_3 = 0
while counter_3 < 20:
    counter_3+=1
    if counter_3 < 15:
        continue
    print(counter_3)