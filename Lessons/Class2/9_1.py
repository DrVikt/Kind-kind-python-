#Подвиг 1. В список:
#a = [5.4, 6.7, 10.4]
#добавить в конец вложенный список со значениями, вводимыми в программу (целые числа вводятся в строчку через пробел). Результирующий список lst вывести на экран командой:
#print(lst)
#Sample Input:
#8 11
#Sample Output:
#[5.4, 6.7, 10.4, [8, 11]]


a = [5.4, 6.7, 10.4]

# здесь продолжайте программу
b = list(map(int, input().split()))
a.append(b)
lst = a
print(lst)