#Подвиг 4. На вход программе подаются оценки студента, записанные через пробел. Необходимо их прочитать и определить, имеется ли в этом списке хотя бы одна оценка ниже тройки. 
#Если это так, то вывести на экран строку "отчислен", иначе - "учится".
#Задачу реализовать с использованием одной из функций: any или all.
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/9/9.9.4
#Sample Input:
#3 3 3 2 3 3
#Sample Output:
#отчислен


# put your python code here
lst_in = list(map(int, input().split()))
print("учится" if all(map(lambda x: x > 2, lst_in)) else "отчислен" )