#Подвиг 4. На вход программе подается четырехзначное целое положительное число. Прочитайте это число и подумайте, как можно определить итератор для перебора его цифр. 
#Выведите все цифры введенного числа (с помощью итератора) в одну строчку через пробел.
#Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/5/5.5.4
#Sample Input:
#4387
#Sample Output:
#4 3 8 7


# put your python code here
a = input()
it = iter(a)
lst = []
d = len(a) 
while d > 0:
    lst.append(next(it))
    d -= 1
print(*lst) 