#Подвиг 7. Используя символы малых букв латинского алфавита (строка ascii_lowercase):
#   from string import ascii_lowercase
#запишите генератор, который бы возвращал все возможные сочетания из двух букв латинского алфавита. Выведите первые 50 сочетаний на экран в строку через пробел.
#Например, первые семь начальных сочетаний имеют вид:
#aa ab ac ad ae af ag


# put your python code here
from string import ascii_lowercase
gen = (x+y for x in ascii_lowercase for y in ascii_lowercase)
lst = []
for i in range(50):
    lst.append(next(gen))
    
print(*lst) 