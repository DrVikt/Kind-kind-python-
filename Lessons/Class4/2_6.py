#Подвиг 7. На вход программе подается натуральное число n. Прочитайте это число и выведите первое найденное натуральное число (то есть, перебирать числа, начиная с 1), 
#квадрат которого больше значения n. Программу реализовать с использованием цикла while.
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/5/5.2.7
#Sample Input:
#10
#Sample Output:
#4


# put your python code here
n = int(input())
i = 1
while i ** 2 <= n:
    i += 1
print(i)