#Подвиг 4. Повторите задачу с транспонированием прямоугольной матрицы с помощью list comprehension, изложенной в видео-уроке к этой практике. 
#На вход программе поступает таблица целых чисел, чтение которой уже реализовано в программе:
#s = sys.stdin.readlines()
#lst_in = [list(map(int, x.strip().split())) for x in s]
#Нужно транспонировать список lst_in (строки заменяются на столбцы) и результат сохранить в списке A. Отобразите полученный список A с помощью следующей конструкции:
#for row in A:
#   print(*row)
#Желательно сделать эту задачу не пересматривая видео.
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/5/5.9.4
#Sample Input:
#1 2 3
#4 5 6
#7 8 9
#5 4 3
#
#Sample Output:
#1 4 7 5
#2 5 8 4
#3 6 9 3


import sys

# считывание списка из входного потока
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

# здесь продолжайте программу (используйте список lst_in)
A = [[lst_in[i][j] for i in range(len(lst_in))] for j in range(len(lst_in[0]))]
for row in A:
    print(*row)