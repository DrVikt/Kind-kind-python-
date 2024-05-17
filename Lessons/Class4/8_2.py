#Подвиг 2. На вход программе подаются целые числа, записанные через пробел. Необходимо их прочитать и с помощью list comprehension сформировать двумерный список lst размером N x N 
#(квадратную таблицу чисел). Гарантируется, что из набора введенных чисел можно сформировать квадратную матрицу (таблицу). Полученный двумерный список отобразить командой:
#print(lst)
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/5/5.9.2
#Sample Input:
#1 2 3 4 5 6 7 8 9
#Sample Output:
#[[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# put your python code here
lst = list(map(int, input().split()))
a =  int(len(lst) ** (1/2))
lst = [[lst[i + k*a]
       for i in range(a)]
       for k in range (a)]
print(lst)