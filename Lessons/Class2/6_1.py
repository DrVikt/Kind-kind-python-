#Подвиг 3. Вводятся три целых числа в одну строку через пробел. Сформируйте список lst, хранящий эти значения в порядке их ввода. Результат выведите на экран, используя команду:
#print(lst)
#Sample Input:
#8 11 3
#Sample Output:
#[8, 11, 3]


# put your python code here
lst = list(map(int, input().split()))
print(lst)