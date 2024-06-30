#Подвиг 6. Из модуля random импортируйте только две функции: seed и random, но у последней должен быть синоним rnd (имя, через которое она будет вызываться в программе). Выполните в программе эти функции, следующим образом:
#seed(10)
#print(round(rnd(), 2))




# put your python code here
from random import seed, random as rnd

seed(10)
print(round(rnd(), 2))