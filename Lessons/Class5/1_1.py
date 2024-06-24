#Подвиг 3. На вход программе подаются данные в формате ключ=значение, записанные через пробел. Значениями здесь являются целые числа (см. пример ниже). 
#Необходимо прочитать строку с этими данными и на их основе сформировать словарь d, используя функцию dict(). Результирующий словарь вывести на экран командой:
#print(*sorted(d.items()))
#Sample Input:
#one=1 two=2 three=3
#Sample Output:
#('one', 1) ('three', 3) ('two', 2)

# put your python code here
lst = input().split()
lst = [x.split('=') for x in lst]
lst = [[k if x == 0 else int(k) for x, k in enumerate(row)] for row in lst]
d = dict(lst)
print(*sorted(d.items()))