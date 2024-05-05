#Подвиг 3. Вводится  матрица чисел из трех строк. В каждой строке числа разделяются пробелом. 
#Необходимо вывести на экран последний столбец этой матрицы в виде строки из трех чисел через пробел.
#Sample Input:
#8 11 12 1
#9 4 36 -4
#1 12 49 5
#Sample Output:
#1 -4 5


# put your python code here
lst = []
lst.append(list(map(int, input().split())))
lst.append(list(map(int, input().split())))
lst.append(list(map(int, input().split())))
print(lst[0][3], lst[1][3], lst[2][3])