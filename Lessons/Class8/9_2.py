#Подвиг 2. На вход программе подаются вещественные числа, записанные через пробел. Необходимо их прочитать и определить, есть ли среди них хотя бы одно отрицательное. Вывести True, если это так и False в противном случае.
#Задачу реализовать с использованием одной из функций: any или all.
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/9/9.9.2
#Sample Input:
#8.2 -11.0 20 3.4 -1.2
#Sample Output:
#True


# put your python code here
lst_in = list(map(float, input().split()))
print(any(map(lambda x: x < 0, lst_in)))