#Подвиг 9. Вводятся оценки студента (числа от 2 до 5) в одну строку через пробел. Необходимо определить количество двоек и вывести это значение на экран.
#Sample Input:
#2 3 5 2 4 2 2 5
#Sample Output:
#4


# put your python code here
lst = list(map(int, input().split()))
print(lst.count(2))