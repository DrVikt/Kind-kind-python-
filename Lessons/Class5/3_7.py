#Подвиг 9. Объявите в программе следующий двумерный кортеж, размером 5 x 5 элементов:
#t = ((1, 0, 0, 0, 0),
#     (0, 1, 0, 0, 0),
#     (0, 0, 1, 0, 0),
#     (0, 0, 0, 1, 0),
#     (0, 0, 0, 0, 1))
#На вход программе подается натуральное число N (N < 5). Необходимо на основе кортежа t сформировать новый аналогичный кортеж t2 размером N x N элементов путем отбрасывания последних строк и столбцов. Результат выведите на экран в виде таблицы чисел.
#P.S. Обратите внимание, что в при выводе таблицы в конце строк не должно быть пробелов.
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/6/6.3.9
#Sample Input:
#3
#Sample Output:
#1 0 0
#0 1 0
#0 0 1


# put your python code here
t = ((1, 0, 0, 0, 0),
     (0, 1, 0, 0, 0),
     (0, 0, 1, 0, 0),
     (0, 0, 0, 1, 0),
     (0, 0, 0, 0, 1))
d = ()
N = int(input())
for i,v in enumerate(t):
    if i < N:
        p = ()
        for k,r in enumerate(v):
            if k < N:
               p += r,
        d += p,
for i in d:
    print(*i)