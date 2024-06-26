#Подвиг 4. На вход программе поступают данные в виде набора строк в формате: 
#ключ1=значение1
#ключ2=значение2
#...
#ключN=значениеN
#Ключами здесь выступают целые числа (см. пример ниже). В программе уже реализовано считывание всех строк и сохранение их в виде списка:
#lst_in = list(map(str.strip, sys.stdin.readlines()))
#Необходимо преобразовать список lst_in в словарь d (без использования функции dict()) и вывести полученный словарь на экран командой:
#print(*sorted(d.items()))
#Sample Input:
#5=отлично
#4=хорошо
#3=удовлетворительно
#Sample Output:
#(3, 'удовлетворительно') (4, 'хорошо') (5, 'отлично')


import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))
# здесь продолжайте программу (используйте список lst_in)
lst = [x.split('=') for x in lst_in]
d = {int(x[0]):x[1] for x  in lst}
print(*sorted(d.items()))