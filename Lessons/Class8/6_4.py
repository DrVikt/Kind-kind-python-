#Подвиг 5. На вход программе поступают две последовательности целых чисел (каждая с новой строки). Длины последовательностей могут быть разными. Необходимо их прочитать и сохранить в отдельных списках или кортежах. 
#Затем, первый список отсортировать по возрастанию, а второй - по убыванию. Полученные пары из обоих списков сложить друг с другом и получить новый список чисел. Результат вывести на экран в виде строки чисел через пробел.
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/9/9.6.5
#Sample Input:
#7 6 4 2 6 7 9 10 4
#-4 5 10 4 5 65
#Sample Output:
#67 14 9 11 10 3


# put your python code here
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = (a + b for a,b in zip(sorted(a), sorted(b, reverse = True)))
print(*c)