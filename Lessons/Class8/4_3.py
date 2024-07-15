#Подвиг 3. На вход программе подаются целые числа, записанные через пробел. Необходимо их прочитать и оставить среди них только двузначные числа. Реализовать программу с использованием функции filter. 
#Результат отобразить на экране в виде последовательности оставшихся чисел в одну строчку через пробел.
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/9/9.4.3
#Sample Input:
#8 11 0 -23 140 1
#Sample Output:
#11 -23


# put your python code here
lst_in = input().split()
a = filter(lambda x: len(x.lstrip('-')) == 2 , lst_in)
print(*a, end = ' ')