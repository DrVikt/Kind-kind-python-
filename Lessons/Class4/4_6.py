#Подвиг 6. На вход программе подаются вещественные числа, записанные через пробел. Необходимо прочитать эти числа и сохранить в списке. 
#Затем, с помощью цикла for нужно найти наименьшее число в этом списке. Полученный результат (минимальное число) вывести на экран.  Реализовать программу без использования функции min, max и сортировки.
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/5/5.4.6
#Sample Input:
#8.6 9.11 -4.567 -10.0 1.45
#Sample Output:
#-10.0


# put your python code here
lst = list(map(float, input().split()))
a = lst[0]
for i in range(1, len(lst)):
    a = a if a < lst[i] else lst[i]
print(a) 