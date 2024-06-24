#Подвиг 8. На вход программе подаются целые числа, записанные в одну строку через пробел. Необходимо их прочитать и сохранить в кортеже. 
#Затем, в кортеже найти и вывести в одну строчку через пробел (по порядку) все индексы неуникальных (повторяющихся) значений.
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/6/6.3.8
#Sample Input:
#5 4 -3 2 4 5 10 11
#Sample Output:
#0 1 4 5


# put your python code here
a = tuple(list(map(int, input().split())))
for i, v in enumerate(a):
    if a.count(v) > 1:
        print(i, end=' ')
